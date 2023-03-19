from .point import Point


class Intersection:
    # https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
    @staticmethod
    def doIntersect(p1, p2, q1, q2) -> Point:
        """Checks if line segment p1p2 intersects with line segment q1q2"""
        dx1 = p2.x - p1.x
        dy1 = p2.y - p1.y
        dx2 = q2.x - q1.x
        dy2 = q2.y - q1.y
        det = dx1*dy2 - dy1*dx2
        if det == 0:
            return None
        else:
            dx3 = q1.x - p1.x
            dy3 = q1.y - p1.y
            t = (dx3*dy2 - dy3*dx2) / det
            u = (dy1*dx3 - dx1*dy3) / det
            if 0 <= t <= 1 and 0 <= u <= 1:
                x = p1.x + t*dx1
                y = p1.y + t*dy1
                return Point(x, y)
            else:
                return None