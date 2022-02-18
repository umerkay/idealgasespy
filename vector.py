import math


class Vector():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def add(self, v):
        self.x += v.x
        self.y += v.y
        return self

    def sub(self, v):
        self.x += v.x
        self.y += v.y
        return self
    
    def mul(self, s):
        self.x *= s
        self.y *= s
        return self

    def mag(self):
        return math.sqrt((self.x) ** 2 + (self.y) ** 2)

    def unit(self):
        self.mul(1/self.mag())
        return self