from typing import Tuple

from .point import Point


class Ground:
    def __init__(self, pts: list[Point]):
        self.ground = pts
        self.n = len(self.ground)
        self.i = self._find_landing()

    def describe(self):
        print("\nGround:")
        for i in range(self.n-1):
            print(f"{self.ground[i]}\t{self.ground[i+1]}\t {i == self.i}")

    def __iter__(self) -> Tuple[Point, Point, bool]:
        for i in range(self.n-1):
            yield self.ground[i], self.ground[i+1], i == self.i

    def get_landing(self) -> Tuple[Point, Point]:
        self.ground[self.i], self.ground[self.i+1]

    def _find_landing(self):
        for i in range(self.n-1):
            if self.ground[i].y == self.ground[i+1].y and self.ground[i+1].x >= self.ground[i].x + 1000:
                return i
        return -1
