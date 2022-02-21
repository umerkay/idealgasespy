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
        self.x -= v.x
        self.y -= v.y
        return self
    
    def mul(self, s):
        self.x *= s
        self.y *= s
        return self
        
    def div(self, s):
        self.x = self.x / s
        self.y = self.y / s
        return self

    def set(self, x, y):
        self.x = x
        self.y = y

    def setV(self, v):
        self.x = v.x
        self.y = v.y
        return self

    def mag(self):
        return math.sqrt((self.x) * (self.x) + (self.y) * (self.y))
        
    def magSq(self):
        return (self.x) * (self.x) + (self.y) * (self.y)

    def unit(self):
        mag = self.mag()        
        return self.div(self.mag()) if mag > 0 else self
    
    def unitSq(self):
        mag = self.magSq()        
        return self.div(self.mag()) if mag > 0 else self