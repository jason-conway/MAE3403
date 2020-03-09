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

    #Computes and returns the pipe flow for the given pressure drop and saves the pressure drop and flow in the delf.dp and self.Q. flow(dp) is the inverse of deltaP(flow)
    def flow(self, dp, rho, mu):

    def display(self):


def pipeFriction(eps, D, Re):
    return (-2 * np.log10((eps / (3.7065 * D)) - ((5.0452 / Re) * np.log10((1 / 2.8257) * (eps / D) ** 1.1098 + (5.8506 / (Re ** .8981)))))) ** -2

def main():
    rho = 1.94; mu = 0.0000186; eps = 0.00082
    p1 = Pipe(6/12, 2000, eps, name = 'a-b')
    pdrop = p1.deltaP(0.75, rho, mu)
    Q = p1.flow(pdrop, rho, mu)
    print(pdrop, Q)
    p1.display()

if __name__ == "__main__": 
    main()