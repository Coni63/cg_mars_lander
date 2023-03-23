from typing import Tuple

from .point import Point


class Ground:
    def __init__(self, pts: list[Point]):
        self.ground = pts
        self.n = len(self.ground)
        self.landing_id = self._find_landing()
        self._length = [self.ground[i].distance(self.ground[i+1]) for i in range(self.n-1)]

    def describe(self):
        print("\nGround:")
        for i in range(self.n-1):
            print(f"{self.ground[i]}\t{self.ground[i+1]}\t {i == self.landing_id}")

    def get_distance(self, crash_point: Point, crash_segment: int) -> float:
        # No need to check the same segment, for it, there is another metric used with speed and angle

        # if we crash on the right of the landing area
        d = 0
        if crash_segment > self.landing_id:
            """
            compute the distance between the rightmost point of the segment and the start of the crash segment
            add the distance between the start of the crash segment and the crash point
            """
            for i in range(self.landing_id+1, crash_segment):
                d += self._length[i]
            d += self.ground[crash_segment].distance(crash_point)
        elif crash_segment < self.landing_id:
            """
            compute the distance between the the crash point and the end of the crash segment
            add the distance between the next segment and the start of the landing segment
            """
            d += self.ground[crash_segment+1].distance(crash_point)
            for i in range(crash_segment+1, self.landing_id):
                d += self._length[i]

        return d

    def __iter__(self) -> Tuple[Point, Point, bool]:
        for i in range(self.n-1):
            yield self.ground[i], self.ground[i+1], i == self.landing_id

    def get_landing(self) -> Tuple[Point, Point]:
        return self.ground[self.landing_id], self.ground[self.landing_id+1]

    def _find_landing(self):
        for i in range(self.n-1):
            if self.ground[i].y == self.ground[i+1].y and self.ground[i+1].x >= self.ground[i].x + 1000:
                return i
        return -1
