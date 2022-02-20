from lib2to3.pgen2.token import OP
from vector import Vector
from particle import Particle
from util import clear
from vars import Options, width, height
from pygame import gfxdraw
import pygame
import sys
import tkinter as tk
import os

# gravity = vector.obj(x = 0, y = 0.5)
# wind = vector.obj(x = 2, y = 0)

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
buttonwin = tk.Frame(root, width = 400, height = 600, bg= "grey")
buttonwin.pack(side="left")
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

button1 = tk.Button(buttonwin,text = 'Reset', command=reset, fg="black", bg= "grey", font= "Times 14 bold")
button1.pack()

root.geometry ("400x600")
# checkboxes
def var_states():
   print (checkVar1.get(), checkVar2.get())
   

tk.Label(buttonwin, text="Checkbox",fg = "black",bg = "grey",font = "Times 16 bold").pack()
checkVar1 = tk.IntVar()
c1 = tk.Checkbutton (buttonwin, text = "ShowElectronCloud" ,fg = "black",bg = "grey",font = "Times 14 bold", variable = checkVar1, onvalue = 1 , offvalue = 0, height = 1 , width=20 )
c1.pack()
checkVar2 = tk.IntVar()
c2 = tk.Checkbutton (buttonwin, text = "Pause" ,fg = "black",bg = "grey",font = "Times 14 bold", variable = checkVar2, onvalue = 1 , offvalue = 0, height = 1 , width=20)
c2.pack()
tk.Button(buttonwin, text='Show Value of checkboxes',fg = "black",bg = "grey",font = "Times 14 bold", command=var_states).pack()

#spinbox
def value_changed():
    print (current_val.get())
tk.Label(buttonwin, text = "Select Temperature",fg="black" , bg= "grey", font= "Times 14 bold").pack()
current_val = tk.IntVar(0) 
spin_temp = tk.Spinbox(buttonwin,from_ = 0 , to= 200 ,textvariable = current_val,wrap = True, command= value_changed, fg= "black" , bg = "grey" , bd =5)
spin_temp.pack()
#dropdown box

#clicked = tk.StringVar()
#def show():
   # myLabel = tk.Label (root, text = clicked.get()).pack()
#myButton = tk.Button (root, text="Select Temperature" , command = show).pack()
#options = ["273" , "300" , "373"]
#clicked.set(options[0])
#drop = tk.OptionMenu (root, clicked , *options  )
#drop.pack()

#Sliders

def show_values():
    print (temp_sli.get(), grav_sli.get())
tk.Label(buttonwin,text= "Temperature(K)",fg = "black",bg = "grey",font = "Times 14 bold").pack()
temp_sli = tk.Scale(buttonwin, from_=0, to=2000 , orient= tk.HORIZONTAL ,bd =5 , bg= "grey")
temp_sli.set(0)
temp_sli.pack()
tk.Label(buttonwin, text= "Gravity",fg = "black",bg = "grey",font = "Times 14 bold").pack()
grav_sli = tk.Scale(buttonwin, from_=0, to=200, orient= tk.HORIZONTAL , bd =5 , bg = "grey")
grav_sli.set(0)
grav_sli.pack()
tk.Button(buttonwin, text='Show value of slider',fg = "black",bg = "grey",font = "Times 14 bold", command=show_values).pack()


#root.geometry("400x400")
#current_value = tk.DoubleVar()
#def slider_changed(event):  
    #print(horizontal.get())

#def slide():
    #my_Label = tk.Label (root, text = horizontal.get()).pack()
    #root.geometry (str(horizontal.get())+"x400")
#my_btn = tk.Button (root, text="Temperature (K)" , command = slider_changed(horizontal)).pack()
#horizontal = tk.Scale(root, from_ = 0 , to = 2000 , orient=tk.HORIZONTAL, variable= current_value ) 
#horizontal.set(Options["temperature"])
#horizontal.pack()
#root.update()
#current_value = tk.DoubleVar()

#horizontal_label = tk.Label( root,text='Slider')

#current_value_label = tk.Label(root,text='Current Value:')
#def get_current_value():
    #return '{: .2f}'.format(current_value.get())

#value_label = tk.Label(root,text=get_current_value)

#def get_slider_changed(event):
    #value_label.configure(text=get_current_value())

#def slide_1():
    #my_Label_1 = tk.Label (root, text = horizontal_1.get()).pack()
    #root.geometry (str(horizontal_1.get())+"x400")
#my_btn_1 = tk.Button (root, text="Gravity" , command = slide_1).pack()
#horizontal_1 = tk.Scale(root, from_ = 0 , to = 200 , orient=tk.HORIZONTAL,variable=current_value,command= slider_changed ) 
#horizontal_1.pack()

#Radiobutton

v = tk.StringVar()
v.set("none")  

constants = [("Pressure","pressure" ),
   	     ("Volume", "volume"),
    	     ("Temperature","temperature"),
             ("None", "none")]

def ShowChoice():
    print(v.get())

tk.Label(buttonwin, text="Choose the Constant Parameter",fg = "black",bg = "grey",font = "Times 16 bold").pack()

for constant, val in constants:
    tk.Radiobutton(buttonwin, text=constant, fg = "black",bg = "grey",font = "Times 14 bold", variable=v,  command=ShowChoice,value=val).pack(anchor=tk.N)
buttonwin.update()

#def sel():
   #selection = "You selected constant "  + str(var.get())
   #label.config(text = selection)
#tk.Label (root, text = "Choose a Constant Parameter: ").pack()
#var = tk.IntVar()
#var.set(1)
#R1 = tk.Radiobutton(root, text="Volume", variable=var, value=1 , command=sel)
#R1.pack( anchor = tk.W )
#R2 = tk.Radiobutton(root, text="Pressure", variable=var, value=2,command=sel)
#R2.pack( anchor = tk.W )
#R3 = tk.Radiobutton(root, text="Temperature", variable=var, value=3,command=sel)
#R3.pack( anchor = tk.W)
#R4 = tk.Radiobutton(root, text="None", variable=var, value=4,command=sel)
#R4.pack( anchor = tk.W)
#label = tk.Label(root, text = var.get())
#label.pack()


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
        loop(surface)
        ###
        screen.blit(surface, (0,0))
        pygame.display.update()
        buttonwin.update()
        ###

reset()
main()