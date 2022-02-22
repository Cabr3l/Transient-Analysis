# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk 
from time import strftime
from PIL import Image, ImageTk

# ça c'est la puissante classse qui contient la methode me permettant de faire varier la taille de l'image avec la taille du frame dans lequel il se trouve
class IMAGE(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open("image.png")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
        
    #fvoici la puissante méthode en question
    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)


class DiagramTabObject(object):
    "Klasse für die Sinus Spannung"
    def __init__(self):
        self.projectTitle = 'Transient Analysis'
        self.frameDiagram = NONE
        
    def showDiagram(self,panelwindow,img_0):
        #Create Frams  

        frameDiagram=ttk.Frame(panelwindow,width=500,height=400, relief=SUNKEN) 
        panelwindow.add(frameDiagram, weight=1)
        cv = IMAGE(frameDiagram)
        cv.pack(fill=BOTH,expand=True)
        self.frameDiagram = frameDiagram #This is done so I can access it elsewhere
        
