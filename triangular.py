from shape import Shape


class Triangular(Shape):
    def area(self) -> float:
        return self.calc_area_triangular(self.points_x, self.points_y)

    def circumference(self) -> float:
        return self.calc_circumference_triangular(self.points_x, self.points_y)

    def draw(self):
        Shape.basic_draw(self.points_x, self.points_y)
