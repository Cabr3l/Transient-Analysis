# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk 
from time import strftime

class ConfigurationObject(object):
    "Klasse für die Sinus Spannung"

    def __init__(self):
        pass
 
    def showConfiguration(self,panelwindowNetworkConfiguration, impedance, amplitude, capacite, pulsation, y0, x1,x2):
        #Create Frames  
        frameConfiguration=ttk.Frame(panelwindowNetworkConfiguration,width=400,height=300, relief=SUNKEN)  
        panelwindowNetworkConfiguration.add(frameConfiguration, weight=1)
        
        frameConfiguration.update()
        frameWidth = frameConfiguration.winfo_width()
        label_impedance=ttk.Label(frameConfiguration, text="Impédance z\u2081 : ", width= int(frameWidth*3/80),anchor=W)
        impe=ttk.Entry(frameConfiguration, textvariable=impedance, width=int(frameWidth*8/80), justify="left")
        ohm= ttk.Label(frameConfiguration, text="[Ohms](\u03A9)",width=int(frameWidth*2/80), justify="right", anchor=W)
        label_impedance.grid(row=1, column=0, pady=3, padx=2)
        impe.grid(row = 1, column=1)
        ohm.grid(row = 1, column = 2)
                
