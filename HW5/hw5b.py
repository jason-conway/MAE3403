from math import *
from copy import *
import matplotlib.pyplot as plt
import numpy as np
from scipy import *

def solveRollingWheel():
    W = 30 #Weight in pounds
    k_g = .8 #Radius of gyration in ft
    r = 1.5 #Radius of wheel in ft
    mu_s = .25 #Coefficient of static friction
    mu_k = .15 #Coefficient of kinetic friction
    theta = 12 #Incline angle in degrees
    gc = 32.2 #Does anyone actually know what g-sub-c is?

    #Array elements correspond with [F, N, a_G, alpha]
    guesses = np.array([0, 0, 0, 0])
    args = W, k_g, r, mu_s, mu_k, theta, gc

    def rollingEquations(x, args):
        guesses, theta = args
        W * sin(theta) - F = (W / gc) * aG




def main():

if __name__ == "__main__": 
    main()