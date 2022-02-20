# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
from time import strftime


class OutputTabObject(object):
    "Klasse für die Sinus Spannung"

    def __init__(self):
        self.projectTitle = 'Transient Analysis'