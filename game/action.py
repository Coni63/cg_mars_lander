from dataclasses import dataclass


@dataclass
class Action:
    thrust: int
    angle: float

    def __str__(self):
        return f"{self.thrust},{self.angle}"
