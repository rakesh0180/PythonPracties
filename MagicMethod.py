class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"{self.x} and {self.y}")

    def __str__(self):
        return (f"({self.x},{self.y})")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)


point = Point(1, 2)
other = Point(1, 2)
print(point == other)
combined = point+other
print("add", point + other)
print("x", combined.x)
print("y", combined.y)
point.draw()
print(point)
