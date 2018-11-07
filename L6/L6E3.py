class Polygon:
    def get_area(self):
        raise NotImplementedError("Необходимо переопределить метод")


class Triangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height / 2


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


if __name__ == "__main__":
    t = Triangle(20.5, 10)
    r = Rectangle(10, 20.5)
    print(t.get_area())
    print(r.get_area())

