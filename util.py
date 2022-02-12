from pygame import gfxdraw

def circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)

def clear(surface):
    surface.fill((0,0,0))