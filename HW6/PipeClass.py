from scipy.optimize import fsolve
import numpy as np

class Pipe:
    def __init__(self, diameter, length, roughness, name = None):
        self.diameter = diameter
        self.length = length
        self.roughness = roughness
        self.name = name
        self.dp = None
        self.Q = None

    #Computes and returns the pipe pressure drop for the given flow and saves the pressure drop and flow in self.dp and self.Q
    def deltaP(self, flow, rho, mu):
        velocity = (4 * flow) / (np.pi * (self.diameter ** 2)) #Calculate the velocity using Jake's Problem's equations
        reynoldsNumber = (rho * abs(velocity) * self.diameter) / mu #Calculate the Reynolds using Jake's Problem's equations
        pipeFriction = friction(self.roughness, self.diameter, reynoldsNumber) #Calculate the pipe friction using Jake's Problem's equations
        self.dp = -(pipeFriction * self.length * abs(velocity) * velocity * rho) / (2 * self.diameter) #Calculate the pressure drop using Jake's Problem's equations
        self.Q = flow #Assign Q with the flow argument
        return self.dp #Return back the pressure drop

    #Computes and returns the pipe flow for the given pressure drop and saves the pressure drop and flow in the delf.dp and self.Q. flow(dp) is the inverse of deltaP(flow)
    def flow(self, dp, rho, mu):
        def findFlow(Q): #Create function to run fsolve on in order to solve for the flow rate
            return (self.deltaP(Q, rho, mu) - dp) #Function should equal zero when the output of deltaP equals the dp argument
        ret = fsolve(findFlow, 1000) #Run fsolve to find the flow rate using an intitial guess of 1000
        self.Q = float(ret) #We want to make this a single float since its returned by fsolve as an array
        self.dp = float(self.dp) #We want to make this a single float since its returned by fsolve as an array
        return self.Q

    def display(self):
        if self.name != None: print('|Pipe Section: {} | '.format(self.name), end = '') #Print out the pipe section name if its not None
        if self.dp != None: print('Pressure Drop: {:.2f} bar | '.format(self.dp), end = '') #Print out the pipe pressure loss if its not None
        if self.Q != None: print('Flow Rate: {:.2f} m^3/second|'.format(self.Q)) #Print out the pipe flow rate if its not None

def friction(roughness, diameter, Re):
    return (-2 * np.log10((roughness / (3.7065 * diameter)) - ((5.0452 / Re) * np.log10((1 / 2.8257) * (roughness / diameter) ** 1.1098 + (5.8506 / (Re ** .8981)))))) ** -2

def main():
    rho = 1.94; mu = 0.0000186; eps = 0.00082
    p1 = Pipe(6/12, 2000, eps, name = 'a-b')
    pdrop = p1.deltaP(0.75, rho, mu)
    Q = p1.flow(pdrop, rho, mu)
    print(pdrop, Q)
    p1.display()

if __name__ == "__main__": 
    main()