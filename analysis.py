# ********************************* #
# Project: Heat Transfer Analysis
# Coder: Alex
# Filename: analysis.py
# Purpose: Contains the analysis script
#          for the entire program. Each analysis
#          is added under its own class.
# ********************************* #

import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.messagebox

# Conduction Analysis
class Conduction:
    # Initializes Conduction analysis GUI
    def __init__(self, subMaster):
        self.subMaster = subMaster
        subMaster.title("Conduction Analysis")

        # Frame
        frame = Frame(subMaster)
        frame.master.geometry("800x600")  # Set the window size
        frame.master.resizable(0, 0)  # Can't change window size
        frame.master.config(bg="white")

        # Create Widgets
        self.createWidgets(subMaster)

    # Creates the input required for analysis
    def createWidgets(self, subMaster):
        analysisLabel = Label(subMaster, text="Conduction Analysis", bg="Black", fg="White")
        analysisLabel.grid(row=0, column=0)
        analysisLabel.config(height=2, font=("Times New Roman", 16))

        # Labels to gather information
        self.Thickness = Label(subMaster, text="Thickness [m]")
        self.Area_s = Label(subMaster, text="Surface Area [m^2]")
        self.Thermal_Cond = Label(subMaster, text="Thermal Conductivity [W/(m*C)]")
        self.Temp_1 = Label(subMaster, text="Higher Temperature [C]")
        self.Temp_2 = Label(subMaster, text="Lower Temperature [C]")

        #User input
        self.L = Entry(subMaster)
        self.A_s = Entry(subMaster)
        self.k = Entry(subMaster)
        self.T_1 = Entry(subMaster)
        self.T_2 = Entry(subMaster)

        # Placing the labels and inputs
        self.Thickness.grid(row=1, sticky=E) # Uses compass as direction (N,E,W,S)
        self.Area_s.grid(row=2, sticky=E)
        self.Thermal_Cond.grid(row=3, sticky=E)
        self.Temp_1.grid(row=4, sticky=E)
        self.Temp_2.grid(row=5, sticky=E)
        self.L.grid(row=1,column=1)
        self.A_s.grid(row=2,column=1)
        self.k.grid(row=3,column=1)
        self.T_1.grid(row=4,column=1)
        self.T_2.grid(row=5,column=1)

        # Calculate Button & Reset Button
        Calculate_Button = Button(subMaster, text="Calculate", command=self.Calculate)
        Calculate_Button.grid(row=7, column=1)
        New_Button = Button(subMaster, text="New Calculation", command=self.Reset)
        New_Button.grid(row=8, column=1)

    # Used to reset the window depending on which analysis
    def Reset(self):
        self.subMaster.destroy()
        self.subMaster = Tk()
        self.app = Conduction(self.subMaster)
        self.subMaster.mainloop()

    # Instruction for the calculate button
    def Calculate(self):
        self.L = self.L.get()
        self.A_s = self.A_s.get()
        self.k = self.k.get()
        self.T_1 = self.T_1.get()
        self.T_2 = self.T_2.get()

        self.conductionAnalysis(self.subMaster)

    # Calculates the basic conduction heat transfer rate per unit time
    def conductionAnalysis(self, subMaster):

        k = float(self.k)
        A_s = float(self.A_s)
        L = float(self.L)
        T_1 = float(self.T_1)
        T_2 = float(self.T_2)

        #Fourier heat law
        Q = k*(A_s)/L * (T_1 - T_2)

        # Displaying results onto GUI
        Label_results = Label(subMaster, text="Results")
        Label_Q = Label(subMaster, text="Heat Transfer Rate [W]: ")
        Label_Q1 = Label(subMaster, text= Q)

        Label_results.grid(row=9, column=0)
        Label_Q.grid(row=10, column=0)
        Label_Q1.grid(row=10, column=1)

        # Initialize Q-delta vector
        Q_delta = []
        N = 100
        L_delta = np.linspace(0, L, num=N)

        # Calculate the heat transfer rate as a function of length
        try:
            for i in range(N):
                Q_calc = k * (A_s) / L_delta[i] * (T_1 - T_2)
                Q_delta.append(Q_calc)
        except RuntimeWarning:
            Q_calc = k * (A_s) / 0.1 * (T_1 - T_2)
            Q_delta.append(Q_calc)

        # Plot data
        figure1 = plt.plot(L_delta,Q_delta)
        plt.xlabel('Length, [m]')
        plt.ylabel('Heat Transfer rate, [W]')
        plt.title('Heat Transfer rate for Conduction')
        plt.show()



# Convection Analysis
class Convection:
    def __init__(self, subMaster):
        self.subMaster = subMaster
        subMaster.title("Convection Analysis")

        # Frame
        frame = Frame(subMaster)
        frame.master.geometry("800x600")  # Set the window size
        frame.master.resizable(0, 0)  # Can't change window size
        frame.master.config(bg="white")

        # Create Widgets onto frame
        self.createWidgets(subMaster)

    # Creates the input required for analysis
    def createWidgets(self, subMaster):
        analysisLabel = Label(subMaster, text="Convection Analysis", bg="Black", fg="White")
        analysisLabel.grid(row=0, column=0)
        analysisLabel.config(height=2, font=("Times New Roman", 16))

        # Labels to gather information
        self.HeatCoeff = Label(subMaster, text="Heat Transfer Coefficient [W/(m^2 * C)]")
        self.HeatCoeff.grid(row=1, column=0, sticky=E)
        # self.HeatCoeff.config(padx=2, pady=2)

        self.SurfaceArea = Label(subMaster, text="Surface Area [m^2]")
        self.SurfaceArea.grid(row=2, column=0, sticky=E)

        self.FluidTemp = Label(subMaster, text="Fluid Temperature [C]")
        self.FluidTemp.grid(row=3, column=0, sticky=E)

        self.SurfaceTemp = Label(subMaster, text="Surface Temperature [C]")
        self.SurfaceTemp.grid(row=4, column=0, sticky=E)

        # User input
        self.h = Entry(subMaster)
        self.A_s = Entry(subMaster)
        self.FluidTempEntry = Entry(subMaster)
        self.SurfaceTempEntry = Entry(subMaster)

        self.h.grid(row=1, column=1)
        self.A_s.grid(row=2, column=1)
        self.FluidTempEntry.grid(row=3, column=1)
        self.SurfaceTempEntry.grid(row=4, column=1)

        # Calculate Button & Reset Button
        Calculate_Button = Button(subMaster, text="Calculate", command=self.Calculate)
        Calculate_Button.grid(row=7, column=1)
        New_Button = Button(subMaster, text="New Calculation", command=self.Reset)
        New_Button.grid(row=8, column=1)

    # Used to reset the window depending on which analysis
    def Reset(self):
        self.subMaster.destroy()
        self.subMaster = Tk()
        self.app = Convection(self.subMaster)
        self.subMaster.mainloop()

    # Instruction for the calculate button
    def Calculate(self):
        self.h = self.h.get()
        self.A_s = self.A_s.get()
        self.FluidTempEntry = self.FluidTempEntry.get()
        self.SurfaceTempEntry = self.SurfaceTempEntry.get()

        self.convectionAnalysis(self.subMaster)

    # Calculates the basic convection heat transfer rate per unit time
    def convectionAnalysis(self, subMaster):

        # Transfer variables
        h = float(self.h)
        A_surface = float(self.A_s)
        Fluid_temp = float(self.FluidTempEntry)
        Surface_temp = float(self.SurfaceTempEntry)


        # Convection equation
        Q_conv = h * A_surface * (Surface_temp - Fluid_temp)


        # Display results on GUI
        Label_results = Label(subMaster, text="Results")
        Label_Q = Label(subMaster, text="Heat Transfer Rate [W]: ")
        Label_Q1 = Label(subMaster, text=Q_conv)

        Label_results.grid(row=9, column=0)
        Label_Q.grid(row=10, column=0)
        Label_Q1.grid(row=10, column=1)





# Pipe Heat Transfer Coefficient Analysis
class HeatTransferCo:
    def __init__(self, subMaster):
        self.subMaster = subMaster
        subMaster.title("Pipe Analysis")

        # Frame
        frame = Frame(subMaster)
        frame.master.geometry("800x600")  # Set the window size
        frame.master.config(bg="white")

        # Create Widgets
        self.createWidgets(subMaster)

    def createWidgets(self, subMaster):
        analysisLabel = Label(subMaster, text="Pipe Heat Transfer Analysis", bg="Black", fg="White")
        analysisLabel.grid(row=0, column=0)
        analysisLabel.config(height=2, font=("Times New Roman", 16))

        # Labels
        self.Temperature = Label(subMaster, text="Fluid Temp [C]")
        self.Temperature.grid(row=1, column=0, sticky=E)

        self.pipeD = Label(subMaster, text="Pipe Diameter [m]")
        self.pipeD.grid(row=2, column=0, sticky=E)

        self.pipeL = Label(subMaster, text="Pipe Length [m]")
        self.pipeL.grid(row=3, column=0, sticky=E)

        self.FminVel = Label(subMaster, text="Min Fluid Velocity [m/s]")
        self.FminVel.grid(row=4, column=0, sticky=E)

        self.FmaxVel = Label(subMaster, text="Max Fluid Velocity [m/s]")
        self.FmaxVel.grid(row=5, column=0, sticky=E)

        self.FIncrement = Label(subMaster, text="Fluid Increment [m/s]")
        self.FIncrement.grid(row=6, column=0, sticky=E)

        # Fluid Properties
        self.PropertiesLabel = Label(subMaster, text="Fluid Properties")
        self.PropertiesLabel.grid(row=7, column=0, sticky=E)
        self.PropertiesLabel.config(bg="black", fg="white")

        self.KinematicViscosity = Label(subMaster, text="Kinematic Viscosity [m^2/s]")
        self.KinematicViscosity.grid(row=8, column=0, sticky=E)

        self.SpecificHeat = Label(subMaster, text="Specific Heat [J/(kg*K)]")
        self.SpecificHeat.grid(row=9, column=0, sticky=E)

        self.ThermalConductivity = Label(subMaster, text="Thermal Conductivity [W/(m*K)]")
        self.ThermalConductivity.grid(row=10, column=0, sticky=E)

        self.DensityLabel = Label(subMaster, text="Density [kg/m^3]")
        self.DensityLabel.grid(row=11, column=0, sticky=E)

        # User Inputs
        self.Temp = Entry(subMaster)
        self.Temp.grid(row=1, column=1)
        self.pipeDiameter = Entry(subMaster)
        self.pipeDiameter.grid(row=2, column=1)
        self.pipeLength = Entry(subMaster)
        self.pipeLength.grid(row=3, column=1)
        self.fluidMin_Vel = Entry(subMaster)
        self.fluidMin_Vel.grid(row=4, column=1)
        self.fluidMax_Vel = Entry(subMaster)
        self.fluidMax_Vel.grid(row=5, column=1)
        self.fluidIncrement = Entry(subMaster)
        self.fluidIncrement.grid(row=6, column=1)
        self.viscosity_kin = Entry(subMaster)
        self.viscosity_kin.grid(row=8, column=1)
        self.Specific_Heat = Entry(subMaster)
        self.Specific_Heat.grid(row=9, column=1)
        self.Conductivity = Entry(subMaster)
        self.Conductivity.grid(row=10, column=1)
        self.Density = Entry(subMaster)
        self.Density.grid(row=11, column=1)

        # Calculate Button & Reset Button
        Calculate_Button = Button(subMaster, text="Calculate", command=self.Calculate)
        Calculate_Button.grid(row=12, column=1)
        New_Button = Button(subMaster, text="New Calculation", command=self.Reset)
        New_Button.grid(row=13, column=1)
        Display_Results = Button(subMaster, text="Display Table", command=self.CreateTable)
        Display_Results.grid(row=14, column=1)

    # Used to reset the window
    def Reset(self):
        self.subMaster.destroy()
        self.subMaster = Tk()
        self.app = HeatTransferCo(self.subMaster)
        self.subMaster.mainloop()

        # Instruction for the calculate button
    def Calculate(self):
        # Gather data from inputs
        self.Temp = self.Temp.get()
        self.pipeDiameter = self.pipeDiameter.get()
        self.pipeLength = self.pipeLength.get()
        self.fluidMin_Vel = self.fluidMin_Vel.get()
        self.fluidMax_Vel = self.fluidMax_Vel.get()
        self.fluidIncrement = self.fluidIncrement.get()
        self.viscosity_kin = self.viscosity_kin.get()
        self.Specific_Heat = self.Specific_Heat.get()
        self.Conductivity = self.Conductivity.get()
        self.Density = self.Density.get()

        # Runs Analysis
        self.HeatTransferCoefficient(self.subMaster)


    def CreateTable(self):
        # Create new window to display results of pipe analysis
        TableWindow = Toplevel(self.subMaster)
        TableWindow.title("Pipe Analysis Results")
        TableWindow.geometry("600x600")

        try:
            # Add main code here
            Label(TableWindow, text="Velocity[m/s]").grid(row=0, column=0)
            Label(TableWindow, text="Nusselt Number").grid(row=0, column=1)
            Label(TableWindow, text="Reynolds Number").grid(row=0, column=2)
            Label(TableWindow, text="Pressure Drop [kPa/10m]").grid(row=0, column=3)
            Label(TableWindow, text="Heat Transfer Coefficient").grid(row=0, column=4)

            # Velocity
            row_index = 1
            for value_vel in self.vel_vec:
                Label(TableWindow, text=value_vel).grid(row=row_index, column=0)
                row_index = row_index + 1

            # Nusselt Number
            row_index = 1
            for value_Nu in self.Nu:
                Label(TableWindow, text=value_Nu).grid(row=row_index, column=1)
                row_index = row_index + 1

            # Reynolds Number
            row_index = 1
            for value_Re in self.Re:
                Label(TableWindow, text=value_Re).grid(row=row_index, column=2)
                row_index = row_index + 1

            # Pressure Drop
            row_index = 1
            for value_P in self.P_delta:
                Label(TableWindow, text=value_P).grid(row=row_index, column=3)
                row_index = row_index + 1

            # Heat Transfer Coefficient
            row_index = 1
            for value_H in self.h:
                Label(TableWindow, text=value_H).grid(row=row_index, column=4)
                row_index = row_index + 1

        except ValueError:
            tkinter.messagebox.showinfo('Window Title', 'Missing Parameters!')
            self.subMaster.destroy()
        except AttributeError:
            tkinter.messagebox.showinfo('Window Title', 'Missing Parameters!')
            self.subMaster.destroy()

        # Analysis
    def HeatTransferCoefficient(self, subMaster):

        Temp = self.Temp
        pipeDiameter = float(self.pipeDiameter)
        fluidMin_Vel = float(self.fluidMin_Vel)
        fluidMax_Vel = float(self.fluidMax_Vel)
        fluidIncrement = float(self.fluidIncrement)
        viscosity_kin = float(self.viscosity_kin)
        Specific_Heat = float(self.Specific_Heat)
        Conductivity = float(self.Conductivity)
        Density = float(self.Density)
        pipeLength = float(self.pipeLength)

        # Constants
        pi = 3.1415

        # Velocity vector using increments
        vel_vec1 = np.arange(start=fluidMin_Vel, stop=fluidMax_Vel, step=fluidIncrement)

        vel_vec = []
        self.vel_vec = vel_vec1

        # Vectors used to hold data
        self.vel_avg = fluidMax_Vel/2 # Average velocity
        self.Re = [] #Reynolds number
        self.lamd = [] # Darcy friction factor
        self.Nu = [] # Nusselt number
        self.h = [] # Heat Transfer Coefficient # [W/(m^2 * C)]
        self.R = [] # Resistance # kg/m^7
        self.P_delta = [] # Pressure drop # Pa

        #Calculate Prantdl number
        prantdl = (Specific_Heat*viscosity_kin)/Conductivity

        # Calculates Reynolds and darcy friction factor into a list
        for vel in self.vel_vec:
            # Reynolds number
            Re_holder = (vel * pipeDiameter)/viscosity_kin
            Re_holder = round(Re_holder, 4)
            self.Re.append(Re_holder)

            # Calculate friction factor
            if Re_holder < 2300:
                # Darcy friction factor
                lamd_holder = 64/Re_holder
                lamd_holder = round(lamd_holder,4)
                self.lamd.append(lamd_holder)
            else:
                lamd_holder = (0.790 * np.log(vel) - 1.64)**(-2.0)
                lamd_holder = round(lamd_holder, 4)
                self.lamd.append(lamd_holder)

        # Calculate Nusselt numbers depending on Reynolds number
        for i in self.Re:
            if i < 2300: # Laminar flow, Re < 2300
                Nu_holder = (3.66**3 + 0.7**3 + ((1.615 * (i * prantdl * pipeDiameter/pipeLength))**(1.0/3.0) - 0.7)**3)**(1.0/3.0)
                Nu_holder = round(Nu_holder, 4)
                self.Nu.append(Nu_holder)

                frict_f_lam = 64 / i
                # Calculate Resistance Factor
                R_holder = (128 * pipeLength * Density * viscosity_kin)/(pipeDiameter**4 * pi * self.vel_avg)
                R_holder = round(R_holder, 4)
                self.R.append(R_holder)

                #Calculate Pressure drop
                # P_holder = (R_holder * (self.vel_avg)**2)/1000
                P_holder = ((frict_f_lam * (pipeLength/pipeDiameter) * (Density/2) * self.vel_avg**2))/(1000*10)
                P_holder = round(P_holder, 4)
                self.P_delta.append(P_holder)

            else: # Turbulent flow, Re >= 2300
                frict_f = (0.790 * np.log(i) - 1.64)**(-2.0) # Friction factor
                Nu_holder = (((frict_f/8) * (i - 1000) * prantdl)/(1+12.7* (frict_f/8)**(1.0/2.0) * ((prantdl)**(2.0/3.0)) - 1)) * (1 + (pipeDiameter/pipeLength)**(2.0/3.0))
                Nu_holder = round(Nu_holder, 4)
                self.Nu.append(Nu_holder)

                #Calculate Resistance Factor
                R_holder = (frict_f * pipeLength * Density * 8)/ (pipeDiameter**5 * pi**2)
                R_holder= round(R_holder, 4)
                self.R.append(R_holder)

                # Calculate Pressure drop
                P_holder = (R_holder * (self.vel_avg)**2)/(1000 * 10)
                P_holder = round(P_holder, 4)
                self.P_delta.append(P_holder)

        # Calculate the Heat transfer Coefficient
        for i in self.Nu:
            h_holder = i * (Conductivity/pipeDiameter)
            h_holder = round(h_holder, 4)
            self.h.append(h_holder)

        # Graph heat transfer as a result of velocity
        figure2 = plt.plot(self.vel_vec, self.h)
        plt.xlabel('Velocity, [m/s]')
        plt.ylabel('Heat Transfer Coefficient, [W/(m^2 * C)]')
        plt.title('Heat Coefficient vs Velocity')
        plt.show()
