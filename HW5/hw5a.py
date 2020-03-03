from math import *
import numpy as np
from scipy.optimize import *

'''
Calculate Reynold's Number for finding the friction
'''
def reynoldsNumber(density, velocity, diameter, viscosity):
    return (density * abs(velocity) * diameter) / viscosity

'''
Approximate the friction through the pipe using the equation provided in Jakes Fluids Problem
''' 
def pipeFriction(roughness, diameter, Re):
    return (-2 * log10((roughness / (3.7065 * diameter)) - ((5.0452 / Re) * log10((1 / 2.8257) * (roughness / diameter) ** 1.1098 + (5.8506 / (Re ** .8981)))))) ** -2

'''
Calculate the velocity of the flow through the pipe
''' 
def velocity(flowrate, diameter):
    return (4 * flowrate) / (pi * (diameter ** 2))

'''
Calculate the pressure drop across the length of pipe
'''
def pressureDrop(friction, length, velocity, density, diameter):
    return (friction * length * abs(velocity) * velocity * density) / (2 * diameter) 

'''
Calculate error between the current guess and the final answer
'''
def flowError(Q, waterDensity, waterViscosity, pipeRoughness, pipeDiameter, pipeLength, Q_a, Q_c):
    deltaP = np.zeros(6) #Create an empty array to store the pressure drops in the pipe sections
    for i in range(6):
        v = velocity(Q[i], pipeDiameter[i]) #Calculate the velocity through the current pipe section
        Re = reynoldsNumber(waterDensity, v, pipeDiameter[i], waterViscosity) #Calculate the Reynold's number through the current pipe section
        friction = pipeFriction(pipeRoughness, pipeDiameter[i], Re) #Calculate the friction through the current pipe section
        deltaP[i] = pressureDrop(friction, pipeLength[i], v, waterDensity, pipeDiameter[i]) #Calculate the pressure drop through the current pipe section

    '''
    Create an array containing the sums of flow into and out of different nodes, as well as the sums of pressure drops in the sub-loops.
    Elements will all equal zero when the individual flowrates are calculated.
    '''
    nodes = [Q_a - Q[0] - Q[1], #Node A
            Q[0] - Q[2] - Q[3], #Node B
            Q[2] - Q_c - Q[4], #Node C
            Q[3] + Q[4] - Q[5], #Node D
            Q[5] + Q[1] - Q[6], #Node E
            deltaP[0] + deltaP[3] + deltaP[5] - deltaP[1], #Pressure loop ABDE
            deltaP[3] - deltaP[4] - deltaP[2]] #Pressure loop BCD
    return nodes

def main():
    waterDensity = 1.94 #Density of water in slug / foot cubed
    waterViscosity = .0000186 #Viscosity of water in lbf-s / foot squared
    pipeRoughness = .00082 #Internal pipe roughness
    Q_a = 2 #Flowrate into node A
    Q_c = 1.4 #Flowrate into node C

    '''
    Array elements correspond with sections [AB, AE, BC, BD, DC, ED]
    '''
    pipeDiameter = np.array([4, 4, 5, 8, 6, 8]) / 12 #Array containing the pipe diameters converted from inches into feet
    pipeLength = np.array([2500, 3000, 3500, 2000, 6000, 1500]) #Array containing the lengths of the pipe sections

    Q_guesses = np.array([1, 1, 1, 1, 1, 1, 1]) #Array containing the initial guesses for Q
    

    flowRates = fsolve(flowError, Q_guesses, args = (waterDensity, waterViscosity, pipeRoughness, pipeDiameter, pipeLength, Q_a, Q_c)) #Use fsolve to calculate the flowrates through all of the pipe sections

    '''
    Display the flowrates through each segment in the system
    '''
    print('The flow through segment AB is {:.3f} cubic feet per second.'.format(flowRates[0]))
    print('The flow through segment AE is {:.3f} cubic feet per second.'.format(flowRates[1]))
    print('The flow through segment BC is {:.3f} cubic feet per second.'.format(flowRates[2]))
    print('The flow through segment BD is {:.3f} cubic feet per second.'.format(flowRates[3]))
    print('The flow through segment DC is {:.3f} cubic feet per second.'.format(flowRates[4]))
    print('The flow through segment ED is {:.3f} cubic feet per second.'.format(flowRates[5]))
    print('The flow out of the system at node E is {:.3f} cubic feet per second.'.format(flowRates[6]))


if __name__ == "__main__": 
    main()