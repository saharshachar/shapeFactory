from shape import Shape


class PointAndLine(Shape):
    def area(self) -> float:
        return 0

    def circumference(self) -> float:
        return 0

    def draw(self):
        Shape.basic_draw(self.points_x, self.points_y)

