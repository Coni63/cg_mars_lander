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
        reward = self.lander.applyMove(action=action, ground=self.ground)
        self.turn += 1

        # game is done when the target is the last checkpoint which is a fictive one aligned with the 2 last ones
        self.done = reward != 0

        return self.lander, self.done

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
