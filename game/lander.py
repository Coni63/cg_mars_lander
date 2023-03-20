from __future__ import annotations

import sys
import math

from .point import Point
from .ground import Ground
from .action import Action
from .intersection import Intersection


class Lander(Point):
    vx: float
    vy: float
    angle: int
    thrust: int
    fuel: float

    def __init__(self, x: int, y: int, vx: float = 0.0, vy: float = 0.0, fuel: int = 0, angle: int = 0, thrust: int = 0):
        super(Lander, self).__init__(x, y)
        self.vx = vx
        self.vy = vy
        self.angle = angle
        self.thrust = thrust
        self.fuel = fuel

    @property
    def speed(self):
        return (self.vx * self.vx + self.vy * self.vy) ** 0.5

    def clone(self) -> Lander:
        return Lander(x=self.x, y=self.y, vx=self.vx, vy=self.vy, angle=self.angle, fuel=self.fuel, thrust=self.thrust)

    def applyMove(self, action: Action, ground: Ground, verbose: bool = False) -> int:
        self._rotate(action.angle)
        self._boost(action.thrust)

        prev_pos = Point(self.x, self.y)
        self._move()
        curr_pos = Point(self.x, self.y)

        info = self._check_landing(prev_pos, curr_pos, ground)
        if "intersection_pt" in info:
            self.x = info["intersection_pt"].x
            self.y = info["intersection_pt"].y

        self._end()
        return info

    def describe(self):  # pragma: no cover
        print("", file=sys.stderr, flush=True)
        print(f"Pod Position       : ({self.x}, {self.y})", file=sys.stderr, flush=True)
        print(f"Pod Speed          : ({self.vx}, {self.vy})", file=sys.stderr, flush=True)
        print(f"Pod Angle          : {self.angle}", file=sys.stderr, flush=True)
        print(f"Pod Thrust         : {self.thrust}", file=sys.stderr, flush=True)
        print(f"Pod Fuel           : {self.fuel}", file=sys.stderr, flush=True)

    def _rotate(self, target_angle: float) -> None:
        # We can't turn more than 15 degrees in one turn
        self.angle += max(min(target_angle - self.angle, 15.0), -15.0)

        # The angle is limited to -90 / 90
        self.angle = max(min(self.angle, 90), -90)

    def _boost(self, thrust: float) -> None:
        # no need to clam the power -- will be in [0, 4]
        if thrust > self.thrust:
            offset = 1
        elif thrust < self.thrust:
            offset = -1
        else:
            offset = 0

        # we need to check with fuel
        self.thrust = min(self.thrust + offset, self.fuel)

    def _is_valid_for_landing(self):
        return self.angle == 0 and abs(self.vx) < 20.5 and abs(self.vy) < 40.5  # finally it is working if the round is below 40 or 20

    def _check_landing(self, prev_pos: Point, curr_pos: Point, ground: Ground) -> dict:
        for i, (p1, p2, is_landing_area) in enumerate(ground):
            pt = Intersection.doIntersect(p1, p2, prev_pos, curr_pos)
            if pt is not None:
                if is_landing_area:
                    if self._is_valid_for_landing():
                        return {
                            "done": True,
                            "valid_landing_area": True,
                            "valid_condition": True,
                            "intersection_pt": pt,
                            "fuel": self.fuel
                        }
                    else:
                        return {
                            "done": True,
                            "valid_landing_area": True,
                            "valid_condition": False,
                            "intersection_pt": pt,
                            "vx": self.vx,
                            "vy": self.vy,
                            "angle": self.angle
                        }
                else:
                    return {
                        "done": True,
                        "intersection_pt": pt,
                        "valid_landing_area": False,
                        "valid_condition": False,
                        "segment_id": i
                    }
        return {
            "done": False
        }

    def _move(self):
        alpha = math.radians(self.angle)
        ax = -self.thrust * math.sin(alpha)
        ay = self.thrust * math.cos(alpha) - 3.711

        self.x += self.vx + 0.5 * ax
        self.y += self.vy + 0.5 * ay

        self.vx += ax
        self.vy += ay

        self.fuel -= self.thrust

    def _end(self):
        return
        self.x = math.trunc(self.x)
        self.y = math.trunc(self.y)
        self.vx = math.trunc(self.vx * 0.85)
        self.vy = math.trunc(self.vy * 0.85)
        self.angle = round(self.angle)
