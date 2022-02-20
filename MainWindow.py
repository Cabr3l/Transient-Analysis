# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk  
from time import strftime
from matplotlib import pyplot as plt
from Menu import MenuObject
from DiagramTab import DiagramTabObject
from NetworkTab import NetworkTabObject
from Configuration import ConfigurationObject
from OutputTab import OutputTabObject
from TransientAnalyze import TransientAnalyzeObject

class MainwindowsObject(object):
    "Klasse für die Sinus Spannung"
    def __init__(self):
        self.projectTitle = 'Transient Analysis'
        self.menuObject = MenuObject()
        self.diagramTabObject = DiagramTabObject()
        self.networkObject = NetworkTabObject()
        self.configurationObject = ConfigurationObject()
        self.outputTab = OutputTabObject()
        self.transientAnalyzeObject =  TransientAnalyzeObject()
        
        
    def StartApp(self):
        # creating tkinter window
        root = Tk()
        #set window size
        root.geometry("1000x500")
        #set title
        root.title(self.projectTitle)
        #Menu
        self.menuObject.showMenu(root)
        
        #Create Paned window  
        panelwindow=ttk.Panedwindow(root, orient=HORIZONTAL)  
        framNetworkConfiguration=ttk.Frame(panelwindow,width=500,height=300, relief=SUNKEN)
        panelwindowNetworkConfiguration=ttk.Panedwindow(framNetworkConfiguration, orient=VERTICAL)
        panelwindow.add(framNetworkConfiguration, weight=1)  
        panelwindow.pack(fill=BOTH, expand=True)  
        panelwindowNetworkConfiguration.pack(fill=BOTH, expand=True)   
        
        #Diagram
        self.diagramTabObject.showDiagram(panelwindow)
        #Configuration
        self.configurationObject.showConfiguration(panelwindowNetworkConfiguration)
        #Network
        self.networkObject.showNetwork(panelwindowNetworkConfiguration)
        
        
        mainloop()
        
