from vars import Options
from vars import width, height
import random
from util import circle, rect
# import vector
from vector import Vector

class Particle():
    def __init__(self, pos = None):
        self.pos = Vector(pos[0], pos[1]) if not(pos == None) else Vector(random.randint(0, width), random.randint(0, height))
        self.vel = Vector(random.randint(-10,10), random.randint(-10,10))
        self.acc = Vector(0, 0)

        self.color = (0, 0, 0)
        self.r = 4
        self.mass = self.r

    def act(self, peers):
        if(Options["Electron Interactions"]):
            
            sumCoh = Vector(0, 0)
            sumRep = Vector(0, 0)

            colliding = False

            for peer in peers:
                if peer!=self:
                    magSq = distSq(peer.pos, self.pos) + 1
                    #cohesion
                    if(not colliding and Options["IMF Coefficient"] > 0):
                        sumCoh.x += (peer.pos.x - self.pos.x) / magSq
                        sumCoh.y += (peer.pos.y - self.pos.y) / magSq
                    #repulsion
                    if magSq < (self.r + peer.r) ** 2:
                        colliding = True
                        sumRep.x += self.pos.x - peer.pos.x
                        sumRep.y += self.pos.y - peer.pos.y

            if(colliding):
                self.vel.x = sumRep.x
                self.vel.y = sumRep.y
            else:
                sumCoh.mul((Options["IMF Coefficient"] * 1000)/((len(peers)**2) * self.mass))
                self.acc.add(sumCoh)

            # colliding = self.repulsion(peers)
            # if(not colliding): self.cohesion(peers)
        self.contain()

    def update(self):
        self.acc.y += Options["gravity"] / 100

        self.vel.add(self.acc)
        #To set a constant temperature
        self.vel = self.vel.unit().mul(Options["temperature"]/100)
        self.pos.add(self.vel)

        self.acc.set(0,0)

    def draw(self, surface):
        if(Options["Show Cloud"]):
            v = self.vel.magSq()
            circle(surface, int(self.pos.x), int(self.pos.y), self.r, (
            min(255, 200 + v),
            100,
            min(255, 255 - v)))
        circle(surface, int(self.pos.x), int(self.pos.y), 1, self.color)

    def contain(self):
        #left
        if (self.pos.x + self.vel.x < self.r):
            self.vel.x *= -1
            self.pos.x = self.r
        #right
        elif (self.pos.x + self.vel.x + self.r > width):
            self.vel.x *= -1
            self.pos.x = width - self.r
        #top
        elif (self.pos.y + self.vel.y < self.r):
            self.vel.y *= -1
            self.pos.y = self.r
        #bottom
        elif (self.pos.y + self.vel.y + self.r > height):
            self.vel.y *= -1
            self.pos.y = height - self.r

    # def cohesion(self, peers):
    #     sum = Vector(0, 0)
    #     temp = Vector(0, 0)
    #     for peer in peers:
    #         if peer!=self:
    #             # pass
    #             # temp.add(peer.pos).sub(self.pos)
    #             # sum.add(temp.div(temp.magSq()))
    #             # temp.set(0, 0)
    #             # sum.add(peer.pos).sub(self.pos)
    #             magSq = (peer.pos.x - self.pos.x) ** 2 + (peer.pos.y - self.pos.y) ** 2
    #             sum.x += (peer.pos.x - self.pos.x) / magSq
    #             sum.y += (peer.pos.y - self.pos.y) / magSq

    #     sum.mul((Options["IMF Coefficient"] * 1000)/((len(peers)**2) * self.mass))
    #     self.acc.add(sum)
        
    # def repulsion(self, peers):
    #     sum = Vector(0, 0)
    #     colliding = False
    #     for peer in peers:
    #         if peer!=self and distSq(self.pos, peer.pos) < self.r ** 2:
    #             colliding = True
    #             sum.add(self.pos).sub(peer.pos)

    #     if(colliding):
    #         sum.unit().mul(self.vel.mag())
    #         self.vel.x = sum.x
    #         self.vel.y = sum.y
    #     return colliding

def distSq(pos1, pos2):
    return (pos1.x - pos2.x) * (pos1.x - pos2.x) + (pos1.y - pos2.y) * (pos1.y - pos2.y)




