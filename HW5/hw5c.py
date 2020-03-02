from math import *
from copy import *
import matplotlib.pyplot as plt
import numpy as np
from scipy import *


def solenoidBehavior():
    m = .002
    k = 8e5
    c = 2
    K_f, K_b = 16, 16
    L_a = 2e-3
    R = 12

    def d_dt(vect, x):
        #vect is a vector such that y=U[0] and z=U[1]. This function should return [y', z']
        return [vect[1],  ]



def main():


if __name__ == "__main__": 
    main()