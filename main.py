
from point_and_line import PointAndLine
from triangular import Triangular
from quadrangle import Quadrangle
from circle import Circle
from rectangle_and_square import RectangleAndSquare


if __name__ == '__main__':
    # new_shape = PointAndLine((1,), (2,))
    # new_shape = PointAndLine((1, 2), (5, 6))
    # new_shape = Triangular((0, 0, 3), (0, 4, 0))
    # new_shape = Quadrangle((3, 1, 2, 4), (5, 1, 19, 0))
    # new_shape = Circle(3, 1, 5)
    # new_shape = RectangleAndSquare((0, 3), (0, 6))

    # print(new_shape.area())
    # print(new_shape.circumference())
    # new_shape.draw()

    # adding areas tryout
    shape1 = Triangular((0, 0, 3), (0, 4, 0))
    shape2 = Quadrangle((3, 1, 2, 4), (5, 1, 19, 0))
    print(f"total area is {shape1.area()} + {shape2.area()} = {shape1 + shape2}")
