# importing only those functions
# which are needed
from asyncio.windows_events import NULL
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk  
from time import strftime
import time
import os
from resizableImage import IMAGE

class NetworkTabObject(object):
    "Klasse für die Sinus Spannung"

    def __init__(self):
        self.projectTitle = 'Transient Analysis'
        self.frameNetwork = NULL
        
    def showNetwork(self,panelwindowNetworkConfiguration):
        #Create Frams  
        frameNetwork=ttk.Frame(panelwindowNetworkConfiguration,width=100,height=80, relief=SUNKEN)
        panelwindowNetworkConfiguration.add(frameNetwork, weight=1)
        self.frameNetwork = frameNetwork
        
        cv=IMAGE(frameNetwork,"circuit.png")
        cv.pack(fill=BOTH, expand=True)
        
    

    
        
