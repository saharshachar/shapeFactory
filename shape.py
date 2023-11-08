from constants import *
from abc import abstractmethod
import matplotlib.pyplot as plt
import math


class Shape:
    def __init__(self, points_x: tuple, points_y: tuple):
        self.points_x = points_x
        self.points_y = points_y

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
    def basic_draw(points_x: tuple, points_y: tuple):
        plt.figure()
        plt.plot([points_x[0], points_x[-1]], [points_y[0], points_y[-1]], LINES_MARKER, markersize=MARKER_SIZE)
        plt.plot(points_x, points_y, LINES_MARKER, markersize=MARKER_SIZE)
        plt.scatter(points_x, points_y)
        plt.title("plotting a shape")
        plt.grid("show")
        plt.show()

    @staticmethod
    def calc_points_distance(point1: tuple, point2: tuple) -> float:
        return math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2))

    @staticmethod
    def calc_area_triangular(points_x: tuple, points_y: tuple) -> float:
        x1, x2, x3 = get_vector_elements(points_x)
        y1, y2, y3 = get_vector_elements(points_y)
        return (1/2) * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

    @staticmethod
    def calc_circumference_triangular(points_x: tuple, points_y: tuple) -> float:
        x1, x2, x3 = get_vector_elements(points_x)
        y1, y2, y3 = get_vector_elements(points_y)
        return Shape.calc_points_distance((x1, y1), (x2, y2)) + \
            Shape.calc_points_distance((x1, y1), (x3, y3)) + \
            Shape.calc_points_distance((x2, y2), (x3, y3))

    ...

    def __add__(self, other) -> float:
        first_area = self.area()
        second_area = other.area()
        return first_area + second_area

