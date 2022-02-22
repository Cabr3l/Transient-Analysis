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
        self.configurationObject = ConfigurationObject(self.diagramTabObject)#This is done so I can plot when I have all the datas
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

        impedance = StringVar()
        amplitude = StringVar()
        capacite = StringVar()
        pulsation = StringVar()
        y0 = StringVar()
        x1,x2 = StringVar(),StringVar()

        #Diagram
        #Here we have to plot the graph

        img_0 = PhotoImage(file="image.png")
        self.diagramTabObject.showDiagram(panelwindow,img_0)
        #Configuration
        self.configurationObject.showConfiguration(panelwindowNetworkConfiguration,impedance, amplitude, capacite,pulsation,y0,x1,x2)
        #Network
        self.networkObject.showNetwork(panelwindowNetworkConfiguration)
        
        
        mainloop()
        
