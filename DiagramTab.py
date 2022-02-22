# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk 
from time import strftime


class DiagramTabObject(object):
    "Klasse für die Sinus Spannung"
    def __init__(self):
        self.projectTitle = 'Transient Analysis'
        self.frameDiagram = NONE
        
    def showDiagram(self,panelwindow,img_0):
        #Create Frams  

        frameDiagram=ttk.Frame(panelwindow,width=500,height=400, relief=SUNKEN) 
        panelwindow.add(frameDiagram, weight=1)
        cv = Canvas(frameDiagram,width = 500, height=400, background="ivory")
        cv.create_image(0,0, anchor=NW, image=img_0)
        cv.grid(row = 0, column=0,padx=10, pady = 10)
        frameDiagram.grid_columnconfigure(0,weight=1)

        self.frameDiagram = frameDiagram #This is done so I can access it elsewhere
        
