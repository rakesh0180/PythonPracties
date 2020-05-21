class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"{self.x} and {self.y}")

    @classmethod
    def zero(cls):
        return cls(1, 3)


abc = Point.zero()
abc.draw()
