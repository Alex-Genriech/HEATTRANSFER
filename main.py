# ********************************* #
# Project: Heat Transfer Analysis
# Coder: Alex
# Filename: main.py
# Purpose: Run the main project loop
# ********************************* #
from gui import *
from analysis import Conduction, Convection, HeatTransferCo


# Run the Conduction Analysis
def ConductionAnalysis():
    subRoot = Tk()
    Conduction(subRoot)
    subRoot.mainloop

# Run the Convection Analysis
def ConvectionAnalysis():
    subRoot = Tk()
    Convection(subRoot)
    subRoot.mainloop

# Run the Heat Transfer Coefficient Analysis for pipe
def HeatTransferCoAnalysis():
    subRoot = Tk()
    HeatTransferCo(subRoot)
    subRoot.mainloop

def main():
    root = Tk()
    b = gui(root)
    root.mainloop()

if __name__ == '__main__':
    main()
