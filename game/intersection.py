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
            u = (dx1*dy3 - dy1*dx3) / det
            if -1 <= t <= 1 and -1 <= u <= 1:
                x = p1.x + t*dx1
                y = p1.y + t*dy1
                return Point(x, y)
            else:
                return None

    # @staticmethod
    # def doIntersect(p1, q1, p2, q2):
    #     # The main function that returns true if
    #     # the line segment 'p1q1' and 'p2q2' intersect.

    #     # Find the 4 orientations required for
    #     # the general and special cases
    #     o1 = Intersection._orientation(p1, q1, p2)
    #     o2 = Intersection._orientation(p1, q1, q2)
    #     o3 = Intersection._orientation(p2, q2, p1)
    #     o4 = Intersection._orientation(p2, q2, q1)

    #     # General case
    #     if ((o1 != o2) and (o3 != o4)):
    #         return True

    #     # Special Cases -- should not exist in this game

    #     # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
    #     if ((o1 == 0) and Intersection._onSegment(p1, p2, q1)):
    #         return True

    #     # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
    #     if ((o2 == 0) and Intersection._onSegment(p1, q2, q1)):
    #         return True

    #     # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
    #     if ((o3 == 0) and Intersection._onSegment(p2, p1, q2)):
    #         return True

    #     # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
    #     if ((o4 == 0) and Intersection._onSegment(p2, q1, q2)):
    #         return True

    #     # If none of the cases
    #     return False

    # @staticmethod
    # def _onSegment(p, q, r):
    #     # Given three collinear points p, q, r, the function checks if
    #     # point q lies on line segment 'pr'
    #     if ( 
    #        (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
    #        (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
    #         return True
    #     return False

    # @staticmethod
    # def _orientation(p, q, r):
    #     # to find the orientation of an ordered triplet (p,q,r)
    #     # function returns the following values:
    #     # 0 : Collinear points
    #     # 1 : Clockwise points
    #     # 2 : Counterclockwise

    #     # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/ 
    #     # for details of below formula.

    #     val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    #     if (val > 0):
    #         # Clockwise orientation
    #         return 1
    #     elif (val < 0):
    #         # Counterclockwise orientation
    #         return 2
    #     else:
    #         # Collinear orientation
    #         return 0
