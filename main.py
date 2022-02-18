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
    particles.extend([Particle() for x in range(50)])

def loop(surface):
    #clear canvas
    clear(surface)

    for particle in particles:
        # particle.applyForce(gravity)
        # particle.applyForce(wind)
        particle.update(particles)
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

# checkboxes

checkVar1 = tk.IntVar()
c1 = tk.Checkbutton (root, text = "ShowElectronCloud" , variable = checkVar1, onvalue = 1 , offvalue = 0, height = 5 , width=20)
c1.pack()
checkVar2 = tk.IntVar()
c2 = tk.Checkbutton (root, text = "Pause" , variable = checkVar1, onvalue = 1 , offvalue = 0, height = 5 , width=20)
c2.pack()
#checkVar3 = tk.IntVar()
#c3 = tk.Checkbutton (root, text = "pause" , variable = checkVar1, onvalue = 1 , offvalue = 0, height = 5 , width=20)
#c3.pack()

#dropdown box

clicked = tk.StringVar()
def show():
    myLabel = tk.Label (root, text = clicked.get()).pack()
myButton = tk.Button (root, text="Select Temperature" , command = show).pack()
options = ["273" , "300" , "373"]
clicked.set(options[0])
drop = tk.OptionMenu (root, clicked , *options  )
drop.pack()

#Sliders

root.geometry("400x400")
def slide():
    my_Label = tk.Label (root, text = horizontal.get()).pack()
    root.geometry (str(horizontal.get())+"x400")
my_btn = tk.Button (root, text="Intermolecularforces" , command = slide).pack()
horizontal = tk.Scale(root, from_ = 0 , to = 200 , orient=tk.HORIZONTAL ) 
horizontal.pack()

def slide_1():
    my_Label_1 = tk.Label (root, text = horizontal_1.get()).pack()
    root.geometry (str(horizontal_1.get())+"x400")
my_btn_1 = tk.Button (root, text="Gravity" , command = slide_1).pack()
horizontal_1 = tk.Scale(root, from_ = 0 , to = 200 , orient=tk.HORIZONTAL ) 
horizontal_1.pack()

#Radiobutton

def sel():
   selection = "You selected constant "  + str(var.get())
   label.config(text = selection)
btn = tk.Button (root, text = "Constant Parameter", command = sel)
btn.pack()
var = tk.StringVar()
R1 = tk.Radiobutton(root, text="Volume", variable=var, value="volume", command=sel)
R1.pack( anchor= tk.W )
R2 = tk.Radiobutton(root, text="Pressure", variable=var, value="pressure",command=sel)
R2.pack( anchor = tk.W )
R3 = tk.Radiobutton(root, text="Temperature", variable=var, value="temperature",command=sel)
R3.pack( anchor = tk.W)
R4 = tk.Radiobutton(root, text="None", variable=var, value="none",command=sel)
R4.pack( anchor = tk.W)
label = tk.Label(root, text = var.get())
label.pack()
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
        clock.tick(600)

        #clear canvas
        loop(surface)
        ###
        screen.blit(surface, (0,0))
        pygame.display.update()
        root.update()
        ###

reset()
main()