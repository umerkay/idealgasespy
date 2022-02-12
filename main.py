import vector
from particle import Particle
from util import clear
from vars import width, height
from pygame import gfxdraw
import pygame
import sys

gravity = vector.obj(x = 0, y = 0.5)
wind = vector.obj(x = 2, y = 0)

#create 100 particles
particles = [Particle() for x in range(100)]

def loop(surface):
    #clear canvas
    clear(surface)

    for particle in particles:
        particle.applyForce(gravity)
        # particle.applyForce(wind)
        particle.update()
        particle.draw(surface)


#ignore beyond this
def main():
    ###
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    ###

    while (True):
        ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        ###

        #run at 30fps
        clock.tick(30)

        #clear canvas
        loop(surface)
        ###
        screen.blit(surface, (0,0))
        pygame.display.update()
        ###

main()