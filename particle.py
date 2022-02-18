from vars import width, height
import random
from util import circle
import vector

class Particle():
    def __init__(self, pos = (width/2, height/2)):
        self.pos = vector.obj(x = random.randint(0, width), y = random.randint(0, height))
        # self.pos = vector.obj(x = pos[0], y = pos[1])
        self.vel = vector.obj(x = 0, y = 0)
        # self.vel = vector.obj(x = random.randint(-10,10), y = random.randint(-10,10))
        self.acc = vector.obj(x = 0, y = 0)

        self.color = (255,255,255)
        self.r = 2
        self.mass = self.r
        self.percRadius = self.r * 10

    def update(self, peers):

        self.cohesion(peers)

        # dont change
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def applyForce(self, force):
        self.acc += force.scale(1/self.mass)

    def draw(self, surface):
        circle(surface, int(self.pos.x), int(self.pos.y), self.r, self.color)
        # circle(surface, int(self.pos.x), int(self.pos.y), self.percRadius, self.color)
    # for i in particle:
    #     pears1=[]
    #     pears2=[]
    #     if i.location<(self.radii)*2:#repulsion function
    #         pears1.append(i)
    #     if i.location<(20):#cohesion function
    #         pears2.append(i)

        

    #  def repulsion(self):
    #     sum=vector()
    #     count=0
    #     for i in pears1:
    #         if i!=self:
    #             diff=self.pos - i.pos#"this" refers to the particle
    #             sum+=diff
    #             count+=1
    #     if count>0:
    #         sum=sum/(count**2)
    #         self.applyforce(sum)

    def cohesion(self, peers):
        sum=vector.obj(x=0,y=0)
        count=0
        for peer in peers:
            if peer!=self and distSq(self.pos, peer.pos) < self.percRadius ** 2:
                diff=vector.obj(x = 0, y = 0)
                diff=peer.pos-self.pos
                sum+=diff
                count+=1
        if count>0:
            sum=sum/(count**10)
            # self.applyforce(sum)
            self.acc += sum.scale(1/self.mass)
    # def collision():

def distSq(pos1, pos2):
    return (pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2




