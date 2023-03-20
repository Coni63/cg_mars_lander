from __future__ import annotations

import json

from .lander import Lander
from .action import Action
from .point import Point
from .ground import Ground


class GameManager:
    data: any
    ground: Ground
    lander: Lander
    turn: int
    done: bool

    def __init__(self):
        self.data = None
        self.ground = []
        self.lander = None
        self.turn = 0
        self.done = False

    def clone(self) -> GameManager:
        copy = GameManager()
        copy.data = self.data
        copy.ground = self.ground  # no need to deepcopy
        copy.lander = self.lander.clone()
        copy.turn = self.turn
        copy.done = self.done
        return copy

    def set_testcase(self, testcase: str):
        with open(testcase, "r") as f:
            self.data = json.load(f)
        self.reset()

        return self.lander, self.ground

    def apply_action(self, action: Action) -> tuple[Lander, bool]:
        data = self.lander.applyMove(action=action, ground=self.ground)
        self.turn += 1

        # game is done when the target is the last checkpoint which is a fictive one aligned with the 2 last ones
        if data["done"]:
            self.done = True
            data = self.get_reward(data)

        # check out of boundary to reduce the search space (all solutions fit in the boundary)
        if self.lander.x < 0 or self.lander.y > 3000 or self.lander.x > 7000:
            self.done = True
            data = {
                "done": True,
                "out_of_boundary": True
            }

        return self.lander, self.done, data

    def reset(self):
        s = self.data["testIn"].split("\n")

        n = int(s[0])

        g = []
        for i in range(1, n+1):
            x, y = [int(x) for x in s[i].split()]
            g.append(Point(x=x, y=y))
        self.ground = Ground(g)

        x, y, hs, vs, f, r, p = [int(i) for i in s[-1].split()]
        self.lander = Lander(x=x, y=y, vx=hs, vy=vs, fuel=f, angle=r, thrust=p)

        self.turn = 0
        self.done = False

    def get_reward(self, data):
        if "out_of_boundary" in data:
            reward = -1e6
        elif data["valid_landing_area"] and data["valid_condition"]:
            reward = data["fuel"]
        elif data["valid_landing_area"] and not data["valid_condition"]:
            reward = -max(abs(data["vx"]) - 20, 0) - max(abs(data["vy"]) - 40, 0) - data["angle"]
        else:
            # it is quite unlikely probable that the reward for a crash on the proper area is below than -300
            reward = -300 - self.ground.get_distance(data["intersection_pt"], data["segment_id"])

        data["reward"] = reward
        return data
