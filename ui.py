from vars import Options
import tkinter as tk
import os

root = tk.Tk()
root.geometry("400x400")
embed = tk.Frame(root, width = 0, height = 0) #creates embed frame for pygame window
embed.grid(columnspan = (500), rowspan = 500) # Adds grid
embed.pack() #packs window to the left

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'


def createButton(name, func):
    button = tk.Button(root,text = name.capitalize(), command=func)
    button.pack()

def valueChanged(w,v,type):
    Options[w] = type(v)

def createSlider(name, min, max, display = ""):
    TempLabel = tk.Label(
        root,
        text=display if not display == "" else name.capitalize()
    )
    TempLabel.pack()

    TempSlider = tk.Scale(
        root,
        from_=min,
        to=max,
        orient='horizontal',
        command=lambda x: valueChanged(name, x, int)
    )
    TempSlider.set(Options[name])
    TempSlider.pack()

def createCheckBtn(name):
    x = tk.IntVar()
    x.set(Options[name])
    CheckBtn = tk.Checkbutton(
        root,
        text=name.capitalize(),
        variable=x,
        command=lambda : valueChanged(name, x.get(), int),
        onvalue=1,
        offvalue=0
    )
    CheckBtn.pack()

    
#ignore beyond this

# checkboxes

# checkVar1 = tk.IntVar()
# c1 = tk.Checkbutton (root, text = "ShowElectronCloud" , variable = checkVar1, onvalue = 1 , offvalue = 0, height = 5 , width=20)
# c1.pack()
# checkVar2 = tk.IntVar()
# c2 = tk.Checkbutton (root, text = "Pause" , variable = checkVar1, onvalue = 1 , offvalue = 0, height = 5 , width=20)
# c2.pack()
#checkVar3 = tk.IntVar()
#c3 = tk.Checkbutton (root, text = "pause" , variable = checkVar1, onvalue = 1 , offvalue = 0, height = 5 , width=20)
#c3.pack()

#dropdown box

# clicked = tk.StringVar()
# def show():
#     myLabel = tk.Label (root, text = clicked.get()).pack()
# myButton = tk.Button (root, text="Select Temperature" , command = show).pack()
# options = ["273" , "300" , "373"]
# clicked.set(options[0])
# drop = tk.OptionMenu (root, clicked , *options  )
# drop.pack()



#Sliders

# def slide():
#     my_Label = tk.Label (root, text = horizontal.get()).pack()
#     root.geometry (str(horizontal.get())+"x400")
# my_btn = tk.Button (root, text="Temperature (K)" , command = slide).pack()
# horizontal = tk.Scale(root, from_ = 0 , to = 2000 , orient=tk.HORIZONTAL ) 
# horizontal.set(Options["temperature"])
# horizontal.pack()

# def slide_1():
#     my_Label_1 = tk.Label (root, text = horizontal_1.get()).pack()
#     root.geometry (str(horizontal_1.get())+"x400")
# my_btn_1 = tk.Button (root, text="Gravity" , command = slide_1).pack()
# horizontal_1 = tk.Scale(root, from_ = 0 , to = 200 , orient=tk.HORIZONTAL ) 
# horizontal_1.pack()

#Radiobutton

# def sel():
#    selection = "You selected constant "  + str(var.get())
#    label.config(text = selection)
# btn = tk.Button (root, text = "Constant Parameter", command = sel)
# btn.pack()
# var = tk.StringVar()
# R1 = tk.Radiobutton(root, text="Volume", variable=var, value="volume", command=sel)
# R1.pack( anchor= tk.W )
# R2 = tk.Radiobutton(root, text="Pressure", variable=var, value="pressure",command=sel)
# R2.pack( anchor = tk.W )
# R3 = tk.Radiobutton(root, text="Temperature", variable=var, value="temperature",command=sel)
# R3.pack( anchor = tk.W)
# R4 = tk.Radiobutton(root, text="None", variable=var, value="none",command=sel)
# R4.pack( anchor = tk.W)
# label = tk.Label(root, text = var.get())
# label.pack()
# root.update()

