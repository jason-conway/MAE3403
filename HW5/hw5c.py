from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import *

'''
Set up differential equations used to model the behavior of the solenoid
'''
def solenoidBehavior(X, time, m, k, c, K_f, K_b, L_a, R, v):
    x, xdot, i = X #Unpack the state array values into their own variables
    xddot = ((-c * xdot) - (k * x) + (K_f * i)) / m #Solve the provided equation for the highest oder term
    idot = (v - (R * i) - (K_b * xdot)) / L_a #Solve the provided equation for the highest order term
    return (xdot, xddot, idot)

def main():
    m = .002 #Mass
    k = 8e5 #Spring constant
    c = 2 #Damping
    K_f, K_b = 16, 16 #Constant
    L_a = 2e-3 #Inductance
    R = 12 #Resistance
    v = 10 #Voltage

    initialConditions = [0, 0, 0] #Initial conditions are 0 per the problem statement
    time = np.linspace(0, .006, 500) #Create 500 points between 0 and .006 seconds. Assignment specifies going between 0 and .015, but in class Delahoussaye said we could adjust it to focus on the interesting parts
    
    ans_c2 = odeint(solenoidBehavior, initialConditions, time, args = (m, k, c, K_f, K_b, L_a, R, v)) #Use odeint to solve the set of differential equations

    '''
    x(t) as a function of time (c = 2)
    '''
    plt.title('x(t) vs time when c = {:d}'.format(c)) #Add a title and lable the axis for the plot
    plt.xlabel('Time [sec]')
    plt.ylabel('Displacement [provided units]')
    plt.plot(time, ans_c2[:,0], 'b', label = 'x(t)') #Add x(t) vs time to the plot
    plt.legend()
    plt.show()

    '''
    i(t) as a function of time (c = 2)
    '''
    plt.title('i(t) vs time when c = {:d}'.format(c)) #Add a title and lable the axis for the plot
    plt.xlabel('Time [sec]')
    plt.ylabel('Current [provided units]')
    plt.plot(time, ans_c2[:,2], 'b', label = 'i(t)') #Add i(t) vs time to the plot
    plt.legend()
    plt.show()

    c = 25 #Change c leaving other parameters unchanged
    ans_c25 = odeint(solenoidBehavior, initialConditions, time, args = (m, k, c, K_f, K_b, L_a, R, v))

    '''
    x(t) as a function of time (c = 25 and 2)
    '''
    plt.title('x(t) vs time for c = 25 and c = 2') #Add a title and lable the axis for the plot
    plt.xlabel('Time [sec]')
    plt.ylabel('Displacement [provided units]')
    plt.plot(time, ans_c25[:,0], 'b', label = 'c = 25') #Add x(t) with c = 25 vs time to the plot
    plt.plot(time, ans_c2[:,0], 'r', label = 'c = 2') #Add x(t) with c = 2 vs time to the plot
    plt.legend()
    plt.show()

    '''
    x(t) with  vs suggested solution
    '''
    plt.title('x(t) with c = 2 vs "suggested solution"') #Add a title and lable the axis for the plot
    plt.xlabel('Time [sec]')
    plt.ylabel('Displacement [provided units]')
    estimatedFcn = (1.67 - (.3 * np.exp(-500 * time) * np.sin(20000 * time + 1.55))) / (10 ** 5) #Find values for the suggested solution provided in the assignment
    plt.plot(time, estimatedFcn, 'b', label = 'Suggested Solution') #Add the suggested solution to the plot
    plt.plot(time, ans_c2[:,0], 'r', label = 'x(t) with c = 2') #Add x(t) with c = 2 vs time to the plot
    plt.legend()
    plt.show()

if __name__ == "__main__": 
    main()