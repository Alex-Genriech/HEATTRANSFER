# ********************************* #
# Project: Heat Transfer Analysis
# Coder: Alex
# Filename: gui.py
# Purpose: Contains the main GUI script
#          for the program
# ********************************* #
from tkinter import *
from main import ConvectionAnalysis, ConductionAnalysis, HeatTransferCoAnalysis

class gui:
    # Main Screen
    def __init__(self, master):
        # ** Main window **
        self.master = master
        master.title("Analysis - Main")

        # Frame
        frame = Frame(master)
        frame.master.geometry("700x500") # Set the window size
        frame.master.resizable(0,0) # Can't change window size
        frame.master.config(bg="white")


        analysisLabel = Label(master, text="Select Analysis", bg="Black", fg="White")
        analysisLabel.pack(fill=X)
        analysisLabel.config(height=2, font=("Times New Roman", 16))

        # ** Buttons on Main window **

        # Conduction Button
        self.conduction = Button(master, text="Conduction", command=ConductionAnalysis)
        self.conduction.place(relx=0.05, rely=0.2, anchor="w")
        self.conduction.config(height=2, width=25)

        # Convection Button
        self.convection = Button(master, text="Convection", command=ConvectionAnalysis)
        self.convection.place(relx=.5, rely=0.2, anchor=CENTER)
        self.convection.config(height=2, width=25)

        # Heat Transfer Coeff Button
        self.HTCoeff = Button(master, text="Heat Transfer Coefficient - Pipe", command=HeatTransferCoAnalysis)
        self.HTCoeff.place(relx=0.95, rely=0.2, anchor="e")
        self.HTCoeff.config(height=2, width=25)

        # # Appendix Button - NO USE CURRENTLY
        # self.Appendix = Button(master, text="Appendix")
        # self.Appendix.place(relx=0.5, rely=0.7, anchor=CENTER)
        # self.Appendix.config(height=2, width=25)

        # Quit Button
        self.quitButton = Button(master, text="Exit", command=master.quit)
        self.quitButton.config(height=2, width=40)
        self.quitButton.place(relx=0.5, rely=.9, anchor=CENTER)











