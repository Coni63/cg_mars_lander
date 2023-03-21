from __future__ import annotations
from dataclasses import dataclass

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .lander import Lander


@dataclass
class Action:
    thrust: int
    angle: int
    relative: bool = False

    def __str__(self):
        return f"{self.angle} {self.thrust}"

    @staticmethod
    def from_str(s, relative=False):
        angle, thrust = [int(x) for x in s.split()]
        # angle = min(max(angle, -15), 15)
        # thrust = min(max(thrust, 0), 4)
        return Action(angle=angle, thrust=thrust, relative=relative)

    @staticmethod
    def convert_to_relative(action: Action, lander: Lander) -> Action:
        delta_angle = action.angle - lander.angle
        angle = min(max(delta_angle, -15), 15)

        delta_thrust = action.thrust - lander.thrust
        thrust = min(max(delta_thrust, -1), 1)
        return Action(angle=int(angle), thrust=int(thrust), relative=True)

    @staticmethod
    def convert_to_absolute(action: Action, lander: Lander) -> Action:
        # no need to check fuel and so on, this is managed by the game engine
        angle = min(max(lander.angle + action.angle, -90), 90)
        thrust = min(max(lander.thrust + action.thrust, 0), 4)
        return Action(angle=angle, thrust=thrust, relative=False)
