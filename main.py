
from abc import abstractmethod
import matplotlib.pyplot as plt
import math

# constants
MARKER_SIZE = 20  # points size when plotting
LINES_MARKER = "b-"       # lines shape and color when plotting


def get_vector_elements(cordi_vector):
    elements = ()
    for curr_cordi in cordi_vector:
        elements = elements + (curr_cordi,)
    return elements

class Shape:
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def circumference(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @staticmethod
    def calc_points_distance(point1, point2):
        return math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2))

    @staticmethod
    def calc_area_triangular(points_x, points_y):
        x1, x2, x3 = get_vector_elements(points_x)
        y1, y2, y3 = get_vector_elements(points_y)
        return (1/2) * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

    @staticmethod
    def calc_circumference_triangular(points_x, points_y):
        x1, x2, x3 = get_vector_elements(points_x)
        y1, y2, y3 = get_vector_elements(points_y)
        return Shape.calc_points_distance((x1, y1), (x2, y2)) + \
            Shape.calc_points_distance((x1, y1), (x3, y3)) + \
            Shape.calc_points_distance((x2, y2), (x3, y3))

class Point_and_line(Shape):
    def __init__(self, points_x, points_y):
        self.points_x = points_x
        self.points_y = points_y

    def area(self):
        return 0

    def circumference(self):
        return 0

    def draw(self):
        Shape.abc(self.points_x, )
        plt.figure()
        plt.plot(self.points_x, self.points_y, LINES_MARKER, markersize=MARKER_SIZE)
        plt.scatter(self.points_x, self.points_y)
        plt.title("plotting a line")
        plt.grid("show")
        plt.show()


class Triangular(Shape):
    def __init__(self, points_x, points_y):
        self.points_x = points_x
        self.points_y = points_y

    def area(self):
        return self.calc_area_triangular(self.points_x, self.points_y)

    def circumference(self):
        return self.calc_circumference_triangular(self.points_x, self.points_y)

    def draw(self):
        plt.figure()
        plt.plot([self.points_x[0], self.points_x[-1]], [self.points_y[0], self.points_y[-1]], LINES_MARKER, markersize=MARKER_SIZE)
        plt.plot(self.points_x, self.points_y, LINES_MARKER, markersize=MARKER_SIZE)
        plt.scatter(self.points_x, self.points_y)
        plt.title("plotting a Triangular")
        plt.grid("show")
        plt.show()


class Quadrangle(Shape):
    def __init__(self, points_x, points_y):
        self.points_x = points_x
        self.points_y = points_y

    def sort_quadrangle_points(self):
        # x1, x2, x3, x4 = points_x
        # y1, y2, y3, y4 = points_y
        zipped_xy = tuple(zip(self.points_x, self.points_y))
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
        # res = list(zip(*return_value))

    def area(self):
        points_x, points_y = list(zip(*self.sort_quadrangle_points()))  # sort the points!
        x1, x2, x3, x4 = points_x
        y1, y2, y3, y4 = points_y
        return Shape.calc_area_triangular([x1, x2, x3], [y1, y2, y3]) \
            + Shape.calc_area_triangular([x1, x3, x4], [y1, y3, y4])

    def circumference(self):
        points_x, points_y = list(zip(*self.sort_quadrangle_points()))  # sort the points!
        x1, x2, x3, x4 = points_x
        y1, y2, y3, y4 = points_y
        return Shape.calc_circumference_triangular([x1, x2, x3], [y1, y2, y3]) \
            + Shape.calc_circumference_triangular([x1, x3, x4], [y1, y3, y4]) \
            - 2 * Shape.calc_points_distance([x1, y1], [x3, y3])

    def draw(self):
        points_x, points_y = list(zip(*self.sort_quadrangle_points()))  # sort the points!
        plt.figure()
        plt.plot([points_x[0], points_x[-1]], [points_y[0], points_y[-1]], LINES_MARKER, markersize=MARKER_SIZE)
        plt.plot(points_x, points_y, LINES_MARKER, markersize=MARKER_SIZE)
        plt.scatter(points_x, points_y)
        plt.title("plotting a quadrangle")
        plt.grid("show")
        plt.show()

if __name__ == '__main__':
    plt.close('all')
    # new_shape = Point_and_line(1, 2)
    # new_shape = Point_and_line((1, 2), (5, 6))
    # new_shape = Triangular((0, 0, 3), (0, 4, 0))

    new_shape = Quadrangle((3, 1, 2, 4), (5, 1, 19, 0))

    print(new_shape.area())
    print(new_shape.circumference())
    new_shape.draw()
