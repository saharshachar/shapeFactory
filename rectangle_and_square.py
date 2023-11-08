from quadrangle import Quadrangle
from shape import Shape


class RectangleAndSquare(Quadrangle):
    @staticmethod
    def extrapolate_4_points(points_x: tuple, points_y: tuple) -> tuple:
        x1, x4 = points_x
        y1, y4 = points_y
        return Quadrangle.sort_quadrangle_points((x1, x1, x4, x4), (y1, y4, y1, y4))

    def area(self) -> float:
        x1, x4 = self.points_x
        y1, y4 = self.points_y
        return abs(x4 - x1) * abs(y4 - y1)

    def circumference(self) -> float:
        x1, x4 = self.points_x
        y1, y4 = self.points_y
        return 2*abs(x4 - x1) + 2*abs(y4 - y1)

    def draw(self):
        points_x, points_y = list(zip(*self.extrapolate_4_points(self.points_x, self.points_y)))  # sort the points!
        Shape.basic_draw(points_x, points_y)


