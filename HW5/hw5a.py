from math import *
from copy import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import *

def pipeFriction(pipeRoughness, pipeDiameter, reynoldsNumber):
    return (-2 * log10((pipeFriction / (3.7065 * pipeDiameter)) - (5.0452 / reynoldsNumber) * log10((1 / 2.8257) * (pipeRoughness / pipeDiameter) ** 1.1098 + (5.8506 / (reynoldsNumber ** .8981))))) ** -2

def velocity(flowrate, diameter):
    return (4 * flowrate) / (pi * (diameter ** 2))

def reynoldsNumber(density, velocity, diameter, viscosity):
    return (density * abs(velocity) * diameter) / viscosity

def pressureDrop(friction, length, velocity, density, diameter):
    return (friction * length * abs(velocity) * velocity * density) / (2 * diameter) 

def flowError(Q, waterDensity, waterViscosity, pipeRoughness, pipeDiameter, pipeLength):
    for i in range(len(Q)):
        deltaP = np.zeros(5)

        velocity = velocity(Q[i], pipeDiameter[i])

        Re = reynoldsNumber(waterDensity, velocity, pipeDiameter[i], waterViscosity)

        friction = pipeFriction(pipeRoughness, pipeDiameter[i], reynoldsNumber[i])

        deltaP[i] = pressureDrop(friction, pipeLength[i], velocity, waterDensity, pipeDiameter[i])

        nodes[0] = 2 - Q[1] - Q[0]
        nodes[1] = Q[0] - Q[2] - Q[3]
        nodes[2] =  Q[2] - 1.4 - Q[4]
        nodes[3] = Q[3] - Q[5] + Q[4]
        nodes[4] = Q[5] + Q[1] - .6

        





def main():
    waterDensity = 1.94
    waterViscosity = .0000186
    pipeRoughness = .00082

    #Array elements correspond with [AB, AE, BC, BD, DC, DE]
    pipeDiameter = np.array([4 / 12, 4 / 12, 5 / 12, 8 / 12, 6 / 12, 8 / 12])
    pipeLength = np.array([2500, 3000, 3500, 2000, 6000, 1500])

    Q = np.array([1, 1, 1, 1, 1, 1])
    flowError = np.array([0, 0, 0, 0, 0, 0])

    args = waterDensity, waterViscosity, pipeRoughness, pipeDiameter, pipeLength
    fsolve()

if __name__ == "__main__": 
    main()