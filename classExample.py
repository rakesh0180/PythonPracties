class MyPoint:
    # def draw(self):
    #     print("draw")

    # def __init__(self):
    #     print("construction")

    def draw(self):
        print(f"draw{self.x} and {self.y}")

    def __init__(self, x, y):
        print("construction")
        self.x = x
        self.y = y


# point = MyPoint()
# point.draw()

point1 = MyPoint(1, 2)
# point1.x = 20
# point1.y = 20
point1.draw()
print(point1.x, point1.y)
print(isinstance(point1, MyPoint))
print(isinstance(point1, int))
