# importing only those functions
# which are needed
from asyncio.windows_events import NULL
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk  
from time import strftime
import time
import os

#cette classe est analogue à la fonction IMAGE du fichier DiagramTab
class IMAGE(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open("circuit.png")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)


class NetworkTabObject(object):
    "Klasse für die Sinus Spannung"

    def __init__(self):
        self.projectTitle = 'Transient Analysis'
        self.frameNetwork = NULL
        
    def showNetwork(self,panelwindowNetworkConfiguration):
        #Create Frams  
        frameNetwork=ttk.Frame(panelwindowNetworkConfiguration,width=100,height=100, relief=SUNKEN)
        panelwindowNetworkConfiguration.add(frameNetwork, weight=1)
        self.frameNetwork = frameNetwork
        cv=IMAGE(frameNetwork)
        cv.pack(fill=BOTH, expand=True)
        
    

    
        
