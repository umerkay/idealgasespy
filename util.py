from pygame import gfxdraw
import pygame

from vars import Options

def circle(surface, x, y, radius, color):
    if(Options["Anti-aliasing"]):
        gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)

def rect(surface, x, y, r, color):
    pygame.draw.rect(surface, color, [x, y, r * 2, r * 2], 2)

def clear(surface):
    surface.fill((255,255,255))