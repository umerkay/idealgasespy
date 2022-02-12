import vector
from particle import Particle
from util import clear
from vars import width, height
from pygame import gfxdraw
import pygame
import sys
import tkinter as tk
import os 

gravity = vector.obj(x = 0, y = 0.5)
wind = vector.obj(x = 2, y = 0)

mouse = {"x": 0, "y": 0, "ax": 0, "ay": 0}
#create 100 particles

particles = []

def reset():
    particles.clear()
    particles.extend([Particle() for x in range(150)])

def loop(surface):
    #clear canvas
    clear(surface)

    for particle in particles:
        particle.applyForce(gravity)
        # particle.applyForce(wind)
        particle.update()
        particle.draw(surface)

def mouseClicked():
    particles.append(Particle(pygame.mouse.get_pos()))

def mouseMoved():
    if(pygame.mouse.get_pressed()[0] == 1):
        particles.append(Particle(pygame.mouse.get_pos()))

#ignore beyond this
root = tk.Tk()
embed = tk.Frame(root, width = 100, height = 100) #creates embed frame for pygame window
embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = "left") #packs window to the left
buttonwin = tk.Frame(root, width = 75, height = 500)
buttonwin.pack(side = "left")
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

button1 = tk.Button(buttonwin,text = 'Reset', command=reset)
button1.pack(side="left")
root.update()

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClicked()
            if event.type == pygame.MOUSEMOTION:
                mouseMoved()
        ###

        #run at 30fps
        clock.tick(30)

        #clear canvas
        loop(surface)
        ###
        screen.blit(surface, (0,0))
        pygame.display.update()
        root.update()
        ###

reset()
main()