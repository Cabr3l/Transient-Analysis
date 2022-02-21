# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk 
from time import strftime
from turtle import width

from sympy import expand

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
        l1, l2,l3= int(frameWidth*3/80),int(frameWidth/10),int(frameWidth*2/80)
        

        ttk.Label(frameConfiguration,text="Données",font="tahoma 17 bold").grid(row=0, column = 0, columnspan=4,pady = 12)

        label_impedance=ttk.Label(frameConfiguration, text="Impédance z\u2081 : ", width= l1,anchor=W)
        impe=ttk.Entry(frameConfiguration, textvariable=impedance,width= l2)
        ohm= ttk.Label(frameConfiguration, text="[Ohms](\u03A9)",width=l3, anchor=W)
        label_impedance.grid(row=1, column=0, pady=10, padx=2,sticky=E)
        impe.grid(row = 1, column=1, sticky=E+W, columnspan=2)
        ohm.grid(row = 1, column = 3, sticky=W)

        label_amplitude=ttk.Label(frameConfiguration, text="Amplitude a : ", width= l1,anchor=W)
        ampli=ttk.Entry(frameConfiguration, textvariable=amplitude,width= l2)
        volts1= ttk.Label(frameConfiguration, text="[Volts](V)",width=l3, anchor=W)
        label_amplitude.grid(row=2, column=0, pady=10, padx=2,sticky=E)
        ampli.grid(row = 2, column=1, sticky=E+W, columnspan=2)
        volts1.grid(row = 2, column = 3, sticky=W)

        label_capacite=ttk.Label(frameConfiguration, text="Capacité C : ", width= l1,anchor=W)
        capa=ttk.Entry(frameConfiguration, textvariable=capacite,width= l2)
        nF= ttk.Label(frameConfiguration, text="[nF]",width=l3, anchor=W)
        label_capacite.grid(row=3, column=0, pady=10, padx=2,sticky=E)
        capa.grid(row = 3, column=1, sticky=E+W, columnspan=2)
        nF.grid(row = 3, column = 3, sticky=W)

        label_pulsation=ttk.Label(frameConfiguration, text="Pulsation w : ", width= l1,anchor=W)
        pulsa=ttk.Entry(frameConfiguration, textvariable=pulsation,width= l2)
        rad_s= ttk.Label(frameConfiguration, text="[rad/s]",width=l3, anchor=W)
        label_pulsation.grid(row=4, column=0, pady=10, padx=2,sticky=E)
        pulsa.grid(row = 4, column=1, sticky=E+W, columnspan=2)
        rad_s.grid(row = 4, column = 3, sticky=W)

        label_y0=ttk.Label(frameConfiguration, text="S initiale : ", width= l1,anchor=W)
        y0_entry=ttk.Entry(frameConfiguration, textvariable=y0,width= l2)
        label_y0.grid(row=5, column=0, pady=10, padx=2,sticky=E)
        y0_entry.grid(row = 5, column=1, sticky=E+W, columnspan=2)
        volts= ttk.Label(frameConfiguration, text="[Volts](V)",width=l3, anchor=W)
        volts.grid(row = 5, column = 3, sticky=W)

        labelDe = ttk.Label(frameConfiguration,text="Tracer de: ", anchor=W)
        x1_entry = ttk.Entry(frameConfiguration,textvariable=x1, width=l3)
        x2_entry = ttk.Entry(frameConfiguration,textvariable=x2, width=l3)
        labelA = ttk.Label(frameConfiguration,text="À")
        labelDe.grid(row = 6, column = 0, pady = 10)
        x1_entry.grid(row = 6, column = 1)
        labelA.grid(row = 6, column =2)
        x2_entry.grid(row=6, column= 3)

        valider = ttk.Button(frameConfiguration,text="VALIDER", command=NONE, width=l3)
        valider.grid(row =7, column =1,pady= 8, columnspan=2)


                
