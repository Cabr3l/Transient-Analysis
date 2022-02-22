# importing only those functions
# which are needed
from re import A
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk 
from time import strftime
from matplotlib import pyplot as plt
import numpy as np
from math import sin, cos, pi, exp

#Fonctions pour la résolution numérique

#Cette fonction renvoie 2 tableaux. Le premier contenant la liste des abscisses, le second contenant la liste des ordonées obtenues par la méthode d'Euler
def Euler(f,tmin,tmax,n,y0,A,B,D,omega):
    pas, i=0,0
    out = np.zeros(n+1)

    pas = (tmax-tmin)/n
    
    out[0] = y0
    t=[tmin+pas*i for i in range(n+1)]
    for i in range(n):
        out[i+1] = out[i]+pas*f(t[i],out[i],A,B,D,omega)
    
    return t,out

#Ici j'implémente la méthode RK4
def RK4(f,tmin,tmax,n,y0,A,B,D,omega):
	pas=(tmax-tmin)/n
	t=[tmin+pas*i for i in range(n+1)]
	out=np.zeros(n+1)
	out[0]=y0

	for i in range(n):
		k1=pas*f(t[i],out[i],A,B,D,omega)
		k2=pas*f(t[i]+0.5*pas,out[i]+0.5*k1,A,B,D,omega)
		k3=pas*f(t[i]+0.5*pas,out[i]+0.5*k2,A,B,D,omega)
		k4=pas*f(t[i]+pas,out[i]+k3,A,B,D,omega)

		out[i+1]=out[i]+(1/6)*(k1+2*k2+2*k3+k4)
	
	return t,out

def f(t,y,A,B,D,omega):
	return A*sin(omega*t)+B*cos(omega*t)-D*y


#cette fonction definit la solution de l'équation homogène

def sh(K,D,t):
	return K*exp(-D*t)

#cette fonction definit la solution particulière de l'équation différentielle

def sp(alpha, beta, w, t):
	return alpha*sin(w*t)+beta*cos(w*t)

#cette fonction définit la solution génerale de notre éqution différentielle

def solution(K,D,alpha, beta, w,t):
	return sh(K,D,t)+sp(alpha, beta, w,t)

class ConfigurationObject(object):
    "Klasse für die Sinus Spannung"

    def __init__(self, diagramTab):
        self.diagramTab = diagramTab


    def plotGraphs(self):
        #Initialition of variables for ploting
        global z1, a,w, C, x_1, x_2, y_0

        z1 = float(self.impedance.get())
        a = float(self.amplitude.get())
        w = float(self.pulsation.get())
        C = float(self.capacite.get())
        x_1 = float(self.x1.get())
        x_2 = float(self.x2.get())
        y_0 = float(self.y0.get())

        #Initialisation of vital variables for ploting
        D=1/(z1*C)
        A=a*D
        B=a*w
        alpha=(A*D+B*w)/(D**2 + w**2)
        beta=(B*D-A*w)/(D**2 + w**2)
        K=y_0-beta
        x=[]
        y=[]
        t0 = x_1

        ####Here is where we define the number of points to be ploted
        n=500
        ######

        pas = (x_2-x_1)/n

        fig=plt.figure(figsize=(5,4))   #ligne où on modifie la taille du screen
        plt.ioff()
        for k in range(n+1):
            x.append(t0)
            y.append(solution(K,D,alpha, beta, w,t0))
            t0+=pas
        t,y_Euler=Euler(f,x_1,x_2,n,solution(K,D,alpha,beta,w,x_1),A,B,D,w)
        t,y_RK4= RK4(f,x_1,x_2,n,solution(K,D,alpha,beta,w,x_1),A,B,D,w)
        plt.plot(x,y)
        plt.plot(t,y_Euler,label="Solution exacte",color="blue", lw=0.5,linestyle="-.")
        plt.plot(t,y_RK4,label=f"Solution approchée par la méthode RK4, h={pas:.2}",lw=0.7,linestyle="--")
        plt.plot(t,y_Euler,label=f"Solution approchée par la méthode Euler, h={pas:.2}",lw=1)
        minAll = min([min(y_Euler),min(y),min(y_RK4)])-0.25*abs(min([min(y_Euler),min(y),min(y_RK4)]))
        maxAll = max([max(y_Euler),max(y),max(y_RK4)])+0.25*abs(max([max(y_Euler),max(y),max(y_RK4)]))
        plt.axis([x_1,x_2,minAll,maxAll])
        plt.legend()
        plt.savefig("courbfig.png")

        #Here I want to plot in the Diargamtab
        #I clear the diagramtab
        for widget in self.diagramTab.frameDiagram.winfo_children():
            widget.destroy

        #I create a canvas in the framediagram of the diagramtab then I put the image in it
        myFrame  = self.diagramTab.frameDiagram
        myCanvas = Canvas(myFrame,width = 500, height= 500)
        img = PhotoImage(file="courbfig.png")
        myCanvas.create_image(0,0,anchor=NW, image = img)
        myCanvas.grid(row = 0 , column = 0)
        myFrame.grid_columnconfigure(0,weight=1)

        plt.show()

    def showConfiguration(self,panelwindowNetworkConfiguration, impedance, amplitude, capacite, pulsation, y0, x1,x2):
        #Instanciating the attributes
        self.impedance = impedance
        self.amplitude = amplitude
        self.capacite = capacite
        self.pulsation = pulsation
        self.y0 = y0
        self.x1 = x1
        self.x2 = x2
        
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
        label_impedance.grid(row=1, column=0, pady=10, padx=2,sticky=E, ipady = 4)
        impe.grid(row = 1, column=1, sticky=E+W, columnspan=2, ipady=4)
        ohm.grid(row = 1, column = 3, sticky=W)

        label_amplitude=ttk.Label(frameConfiguration, text="Amplitude a : ", width= l1,anchor=W)
        ampli=ttk.Entry(frameConfiguration, textvariable=amplitude,width= l2)
        volts1= ttk.Label(frameConfiguration, text="[Volts](V)",width=l3, anchor=W)
        label_amplitude.grid(row=2, column=0, pady=10, padx=2,sticky=E)
        ampli.grid(row = 2, column=1, sticky=E+W, columnspan=2,ipady=4)
        volts1.grid(row = 2, column = 3, sticky=W)

        label_capacite=ttk.Label(frameConfiguration, text="Capacité C : ", width= l1,anchor=W)
        capa=ttk.Entry(frameConfiguration, textvariable=capacite,width= l2)
        nF= ttk.Label(frameConfiguration, text="[nF]",width=l3, anchor=W)
        label_capacite.grid(row=3, column=0, pady=10, padx=2,sticky=E)
        capa.grid(row = 3, column=1, sticky=E+W, columnspan=2,ipady=4)
        nF.grid(row = 3, column = 3, sticky=W)

        label_pulsation=ttk.Label(frameConfiguration, text="Pulsation w : ", width= l1,anchor=W)
        pulsa=ttk.Entry(frameConfiguration, textvariable=pulsation,width= l2)
        rad_s= ttk.Label(frameConfiguration, text="[rad/s]",width=l3, anchor=W)
        label_pulsation.grid(row=4, column=0, pady=10, padx=2,sticky=E)
        pulsa.grid(row = 4, column=1, sticky=E+W, columnspan=2,ipady=4)
        rad_s.grid(row = 4, column = 3, sticky=W)

        label_y0=ttk.Label(frameConfiguration, text="S initiale : ", width= l1,anchor=W)
        y0_entry=ttk.Entry(frameConfiguration, textvariable=y0,width= l2)
        label_y0.grid(row=5, column=0, pady=10, padx=2,sticky=E)
        y0_entry.grid(row = 5, column=1, sticky=E+W, columnspan=2,ipady=4)
        volts= ttk.Label(frameConfiguration, text="[Volts](V)",width=l3, anchor=W)
        volts.grid(row = 5, column = 3, sticky=W)

        labelDe = ttk.Label(frameConfiguration,text="Tracer de: ", anchor=W)
        x1_entry = ttk.Entry(frameConfiguration,textvariable=x1, width=l3)
        x2_entry = ttk.Entry(frameConfiguration,textvariable=x2, width=l3)
        labelA = ttk.Label(frameConfiguration,text="À")
        labelDe.grid(row = 6, column = 0, pady = 10)
        x1_entry.grid(row = 6, column = 1,ipady=4)
        labelA.grid(row = 6, column =2)
        x2_entry.grid(row=6, column= 3,ipady=4)

        valider = ttk.Button(frameConfiguration,text="VALIDER", command=self.plotGraphs, width=l3)
        valider.grid(row =7, column =1,pady= 8, columnspan=2,ipady=4)

        frameConfiguration.grid_columnconfigure(1,weight=1)
        frameConfiguration.grid_rowconfigure(0,weight=1)
        frameConfiguration.grid_rowconfigure(1,weight=1)
        frameConfiguration.grid_rowconfigure(2,weight=1)
        frameConfiguration.grid_rowconfigure(3,weight=1)
        frameConfiguration.grid_rowconfigure(4,weight=1)
        frameConfiguration.grid_rowconfigure(5,weight=1)
        frameConfiguration.grid_rowconfigure(6,weight=1)
        frameConfiguration.grid_rowconfigure(7,weight=1)



                
