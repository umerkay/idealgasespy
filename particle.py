from vars import width, height
import random
from util import circle
import vector

class Particle():
    def __init__(self, pos = (width/2, height/2)):
        self.pos = vector.obj(x = pos[0], y = pos[1])
        self.vel = vector.obj(x = random.randint(-10,10), y = random.randint(-10,10))
        self.acc = vector.obj(x = 0, y = 0)

        self.color = (255,255,255)
        self.r = 2
        self.mass = self.r

    def update(self):

        self.contain()

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def applyForce(self, force):
        self.acc += force.scale(1/self.mass)

    def draw(self, surface):
        circle(surface, int(self.pos.x), int(self.pos.y), self.r, self.color)

    def contain(this):
        if (this.pos.x + this.vel.x < this.r):
            this.vel.x *= -1
            this.pos.x = this.r

        elif (this.pos.x + this.vel.x > width - this.r):

            this.vel.x *= -1
            this.pos.x = width - this.r

        elif (this.pos.y + this.vel.y < this.r):

            this.vel.y *= -1
            this.pos.y = this.r

        elif (this.pos.y + this.vel.y > height - this.r):

            this.vel.y *= -1
            this.pos.y = height - this.r