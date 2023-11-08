from shape import Shape
from triangular import Triangular

class Quadrangle(Shape):
    @staticmethod
    def sort_quadrangle_points(points_x: tuple, points_y: tuple) -> tuple:
        zipped_xy = tuple(zip(points_x, points_y))
        points_xy = sorted(zipped_xy, key=(lambda pair: pair[1]))
        x_sorted = [x for x, y in points_xy]
        y_sorted = [y for x, y in points_xy]

        # switch point 3 and 4
        temp_save = x_sorted[2]
        x_sorted[2] = x_sorted[3]
        x_sorted[3] = temp_save

        temp_save = y_sorted[2]
        y_sorted[2] = y_sorted[3]
        y_sorted[3] = temp_save

        return tuple(zip(x_sorted, y_sorted))

    def area(self) -> float:
        points_x, points_y = list(zip(*Quadrangle.sort_quadrangle_points(self.points_x,
                                                                         self.points_y)))  # sort the points!
        x1, x2, x3, x4 = points_x
        y1, y2, y3, y4 = points_y
        return Shape.calc_area_triangular((x1, x2, x3), (y1, y2, y3)) \
            + Shape.calc_area_triangular((x1, x3, x4), (y1, y3, y4))

    def circumference(self) -> float:
        points_x, points_y = \
            list(zip(*Quadrangle.sort_quadrangle_points(self.points_x, self.points_y)))  # sort the points!
        x1, x2, x3, x4 = points_x
        y1, y2, y3, y4 = points_y
        return Shape.calc_circumference_triangular((x1, x2, x3), (y1, y2, y3)) \
            + Shape.calc_circumference_triangular((x1, x3, x4), (y1, y3, y4)) \
            - 2 * Shape.calc_points_distance((x1, y1), (x3, y3))

    def draw(self):
        points_x, points_y = \
            list(zip(*Quadrangle.sort_quadrangle_points(self.points_x, self.points_y)))  # sort the points!
        Shape.basic_draw(points_x, points_y)
