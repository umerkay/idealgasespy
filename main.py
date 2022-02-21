from lib2to3.pgen2.token import OP
from tkinter import font
from vector import Vector
from particle import Particle
from util import clear
from vars import Options, width, height
from pygame import gfxdraw
import pygame
import sys
from ui import createButton, createCheckBtn, createSlider, root

mouse = {"x": 0, "y": 0, "ax": 0, "ay": 0}

particles = []

def reset():
    particles.clear()
    particles.extend([Particle() for x in range(100)])

def loop(surface, clock):
    clear(surface)

    for particle in particles:
        particle.act(particles)
        particle.update()
        particle.draw(surface)

def mouseClicked():
    particles.append(Particle(pygame.mouse.get_pos()))

def mouseMoved():
    if(pygame.mouse.get_pressed()[0] == 1):
        particles.append(Particle(pygame.mouse.get_pos()))

createButton("reset", reset)

createCheckBtn("Show Cloud")
createCheckBtn("Electron Interactions")
createCheckBtn("Anti-aliasing")

createSlider("temperature", 0, 1000, "Temperature (K)")
createSlider("IMF Coefficient", 0, 200)
createSlider("gravity", 0, 50)

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
        clock.tick(60)

        #clear canvas
        loop(surface, clock)
        ###
        screen.blit(surface, (0,0))
        pygame.display.update()
        root.update()
        ###

reset()
main()