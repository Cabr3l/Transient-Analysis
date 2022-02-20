# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk 
from time import strftime


class ConfigurationObject(object):
    "Klasse für die Sinus Spannung"

    def __init__(self):
        self.projectTitle = 'Transient Analysis'
        
    def showConfiguration(self,panelwindowNetworkConfiguration):
        #Create Frams  
        frameConfiguration=ttk.Frame(panelwindowNetworkConfiguration,width=400,height=300, relief=SUNKEN)  
        panelwindowNetworkConfiguration.add(frameConfiguration, weight=1)
        