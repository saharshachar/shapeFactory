from shape import Shape
import matplotlib.pyplot as plt
import math


class Circle(Shape):
    def __init__(self, radius: float, center_x: float, center_y: float):
        assert radius > 0, "radius must be positive"
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y

    def area(self) -> float:
        return math.pi * math.pow(self.radius, 2)

    def circumference(self) -> float:
        return 2 * math.pi * self.radius

    def draw(self):
        circle1 = plt.Circle((self.center_x, self.center_y), self.radius, color='b', fill=False)
        ax = plt.gca()
        ax.cla()  # clear things for fresh plot

        # change default range so that new circles will work
        ax.set_xlim((self.center_x - self.radius, self.center_x + self.radius))
        ax.set_ylim((self.center_y - self.radius, self.center_y + self.radius))

        ax.add_patch(circle1)
        plt.show()
