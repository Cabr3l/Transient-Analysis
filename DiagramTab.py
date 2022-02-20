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
        
    def showDiagram(self,panelwindow):
        #Create Frams  
        frameDiagram=ttk.Frame(panelwindow,width=500,height=400, relief=SUNKEN) 
        panelwindow.add(frameDiagram, weight=1)
        