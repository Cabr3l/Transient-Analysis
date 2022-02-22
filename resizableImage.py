from tkinter import *
from tkinter.ttk import *
from tkinter import ttk 
from time import strftime
from PIL import Image, ImageTk


# ça c'est la puissante classse qui contient la methode me permettant de faire varier la taille de l'image avec la taille du frame dans lequel il se trouve
class IMAGE(Frame):
    def __init__(self, master,nom):
        Frame.__init__(self, master)

        self.image = Image.open(f"{nom}")
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

