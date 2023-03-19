from dataclasses import dataclass


@dataclass
class Action:
    thrust: int
    angle: float

    def __str__(self):
        return f"{self.thrust},{self.angle}"

    @staticmethod
    def from_str(s):
        angle, thrust = [int(x) for x in s.split()]
        # angle = min(max(angle, -15), 15)
        # thrust = min(max(thrust, 0), 4)
        return Action(angle=angle, thrust=thrust)
