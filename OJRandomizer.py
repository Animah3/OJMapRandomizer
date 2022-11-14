import tkinter as tk
from tkinter import *
import random
from PIL import ImageTk, Image

counter = 0
def donothing():
   x =0


def openNewWindow():

   mapInt = random.randint(0,len(maps)-1)
   mapChoice = maps[mapInt]

   # Toplevel object which will
   # be treated as a new window
   newWindow = Toplevel(root)

   # sets the title of the
   # Toplevel widget
   newWindow.title("New Window")

   # sets the geometry of toplevel
   newWindow.geometry("200x200")

   # A Label widget to show in toplevel
   Label(newWindow,
         text=mapChoice).pack()


def mapChoose():
   global mapChoice
   global maps
   if(len(maps) == 00):
      label.config(text=('No More Maps. Please Reset!!! Last Map Was: ' + mapChoice))
      return 1
   mapInt = random.randint(0,len(maps)-1)
   mapChoice = maps[mapInt]
   maps.remove(mapChoice)
   global counter
   counter += 1

   # A Label widget to show in toplevel
   label.config(text=mapChoice)
   rollLabel.config(text=('Roll Number: ' + str(counter)))

def mapReset():
   global maps
   maps=['Clover',
           'White Winter',
           'Star Circuit',
           'Training Program',
           'Frost Cave',
           'Shipyard',
           'Fungus Cave',
           'Practice Field',
           'Space Wanderer',
           'Pudding Chase',
           'Christmas Miracle',
           'Planet Earth',
           'Sealed Archive']

maps = ['Clover',
'White Winter',
'Star Circuit',
'Training Program',
'Frost Cave',
'Shipyard',
'Fungus Cave',
'Practice Field',
'Space Wanderer',
'Pudding Chase',
'Christmas Miracle',
'Planet Earth',
'Sealed Archive']
root = tk.Tk()
root.geometry("500x500")
root.title("Tei's Map Randomizer")

root.iconbitmap('teiFace.ico')
img = ImageTk.PhotoImage(Image.open('latest.png'))
imgLabel = Label(root, image = img)





btn = Button(root, text ='Select a Map!!!', bd = '5', command = mapChoose)
btn.pack(side = 'top')
label = tk.Label(text="No Map Chosen")
label.pack()
rollLabel = tk.Label(text=('Roll Number: ' + str(counter)))
rollLabel.pack()
imgLabel.pack()
RstBtn = Button(root, text ='Reset Map List!!!', bd = '5', command = mapReset)
RstBtn.pack()

root.mainloop()