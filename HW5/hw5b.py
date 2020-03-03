from math import *
import numpy as np
from scipy.optimize import *

'''
Uses the equations provided in "Rolling Wheel Dynamics for Fsolve" to find F, N, a_G, alpha, and theta
'''
def solveRollingWheel(currentGuess, args):
    F, N, a_G, alpha, theta = currentGuess #Unpack the current guess array 
    W, r, k_g, gc, mu_s = args #Unpack args to use the necessary values
    return  [(W / gc) * a_G + F - W * sin(theta), #F
              N - W * cos(theta), #N
              -1 * F * r + (W / gc) * (k_g ** 2) * alpha, #a_G
              r * alpha - a_G, #alpha
              F - mu_s * N] #theta

def main():
    W = 30 #Weight in pounds
    k_g = .8 #Radius of gyration in ft
    r = 1.5 #Radius of wheel in ft
    mu_s = np.array([.29, .65]) #Coefficients of static friction to find theta at
    gc = 32.2 #G-sub-c is fake news. Change my mind

    '''
    Array elements correspond with [F, N, a_G, alpha, theta]
    '''

    initialGuesses = np.zeros(5) #Create an empty array containing the intitial guesses for fsolve

    for i in range(len(mu_s)): #Loop through the available values of mu
        knowns = np.array([W, r, k_g, gc, mu_s[i]]) #Create an array to pass to solveRollingWheel with args
        solution = fsolve(solveRollingWheel, initialGuesses, args = knowns) #Use fsolve to calculate F, N, a_G, alpha, and theta
        print('The maximum no-slip ramp angles associated with a coefficient of static friction of {:.3f} is {:3f} degrees.'.format(mu_s[i], solution[4] / pi * 180)) #Print the current coefficient of friction and associated no-slip angle

if __name__ == "__main__": 
    main()