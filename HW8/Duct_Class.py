'''Import... everything?'''
import sys
from scipy.optimize import fsolve
import numpy as np
from math import *
from copy import deepcopy

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

class Fitting:
    def __init__(self):
        self.ID = None
        self.type = None
        self.upfittingID = None
        self.upfitting = None
        self.data = None
        self.length = 0
        self.flow = None

class Duct:
    def __init__(self):
        self.title = None
        self.fanPressure = None
        self.airDensity = None
        self.roughness = None
        self.rounding = None
        self.fittings = []
        self.longestRunVal = -(2**64)
        self.longestRunDiffuser = None
        self.longestRunPath = None

    def ReadDuctData(self, data):
        for row in data:
            column = row.strip().split(',') #Break the row of data into several columns
            keyword = column[0].lower() #Specifiy the first column as keyword
            
            '''Grab HVAC Model Parameters from the Input Data File'''
            if keyword == "title": 
                self.title = column[1].strip() #Update title from the input file
            if keyword == "fan_pressure": 
                self.fanPressure = column[1].strip() #Update fan pressure from the input file
            if keyword == "air_density": 
                self.airDensity = column[1].strip() #Update air density from the input file
            if keyword == "roughness": 
                self.roughness = column[1].strip() #Update roughness from the input file
            if keyword == "rounding": 
                self.rounding = column[1].strip() #Update rounding from the input file

            '''Handle the Model Fitting Types and Associated Data'''
            if keyword == "fitting": 
                fitting = Fitting() #Create object fitting

                fitting.ID = column[1].strip() #Apply the fitting ID to the object
                fitting.type = column[2].strip() #Apply the fitting type to the object
                
                if fitting.type.lower() != "air_handling_unit": #Air Handling Unit has no fan-side-ID or flow/length
                    '''Split Fan-Side-ID's When Possible'''
                    fitting.upfittingID = column[3].strip().split('-')[0]
                    

                    if fitting.type.lower() == "duct": 
                        fitting.length = float(column[4].strip()) #Apply the fitting length to the object
                        fitting.data = fitting.length

                    if fitting.type.lower() == "diffuser": 
                        fitting.flow = float(column[4].strip()) #Data in column 4 represents length when type is duct or diffuser
                        fitting.data = fitting.flow

                    '''Note that no extra data needs to be read if type is tee or elbow'''
                
                self.fittings.append(fitting)

        self.UpdateConnections() #Go back and update upfitting with the corresponding type for upfittingIF

    def UpdateConnections(self):
        for fitting in self.fittings:
            fitting.upfitting = FindFittingByID(fitting.upfittingID, self.fittings)

    def FindLongestRun(self):
        self.longestRunVal = -(2**64) #Init longestRunVal with "really really" small number
        self.longestRunDiffuser = None
        for fitting in self.fittings:
            if fitting.type.lower() == 'diffuser':
                path, distance = self.PathToFan(fitting)
                if distance > self.longestRunVal:
                    self.longestRunVal = distance
                    self.longestRunDiffuser = fitting.ID
                    self.longestRunPath = path
            
    def PathToFan(self, fitting):
        if fitting.upfitting == None: return fitting.ID, 0
        else: return (fitting.ID + ', ' + self.PathToFan(fitting.upfitting)[0]), (fitting.length + self.PathToFan(fitting.upfitting)[1])

    def GenerateReport(self):
        report = 'Title:\t\t'+ self.title
        report += '\nFan Pressure:\t'+ str(self.fanPressure)
        report += '\nAir Density:\t\t'+ str(self.airDensity)
        report += '\nRoughness:\t\t'+ str(self.roughness)
        report += '\nRounding:\t\t'+ str(self.rounding)
        report += '\n\n---------------------------- Fitting Summary ---------------------------------'
        report += '\n\nFitting\tType\t\tUpstream-Fitting\tData\n\n'
        
        for fitting in self.fittings:
            if fitting.type == 'Air_Handling_Unit': report += '{:}\t{:}\t{:}\t\t{:}\n'.format(fitting.ID, fitting.type, fitting.upfittingID, fitting.data)
            elif fitting.type != 'Air_Handling_Unit': report += '{:}\t{:}\t\t{:}\t\t{:}\n'.format(fitting.ID, fitting.type, fitting.upfittingID, fitting.data)
        report += '\n\n'
        return report

    
def FindFittingByID(ID, fittinglist):
    for fitting in fittinglist: #Loop through fittinglist with "fitting" as our index
        if fitting.ID == ID: #ID of the current fitting matched our argument
            return fitting #Return back the fitting
    return None #Fitting wasn't found in fittinglist

def main():
    # f1 = open('/Users/jasonconway/Documents/GitHub/MAE3403/HW8/Duct Design Input File 1.txt', 'r')
    f1 = open('Duct Design Input File 1.txt', 'r') #Open the file as read-only
    data = f1.readlines() #Read the entire file as a list of strings
    f1.close() #Close the file we opened

    duct = Duct() #Create opject "duct"
    duct.ReadDuctData(data)
    duct.FindLongestRun()
    print("The longest path is: ", duct.longestRunPath)

if __name__ == "__main__":
    main()    