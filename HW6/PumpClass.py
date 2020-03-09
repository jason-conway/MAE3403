from scipy.optimize import fsolve

class Pump:
    def __init__(self, cvals):
        self.C = cvals #Coefficients of a cubic equation
        self.dp = None
        self.Q = None

    #Computes and returns the pump exit pressure for the given flow and saves the pressure and flow in self.dp and self.Q
    def deltaP(self, Q):
        self.Q = Q
        c = self.C
        self.dp = (((c[3] * Q) + c[2]) * Q + c[1]) * Q + c[0]
        return self.dp

    #Computes and returns the pump flow for the given pump pressure and saves the pressure drop and flow and self.dp and self.Q. flow(dp) is the inverse of deltaP(flow)
    def flow(self, dp):

def main():
    import numpy as np
    import matplotlib.pyplot as plt

    p1 = Pump([15000, -1820, -12900, -15150]) #Create the pump object
    dp = p1.deltaP(0.5) #Pressure output for flow = 0.5
    Q = p1.flow(dp) #Flow at that pressure should be 0.5
    print(dp, Q)

    flows = np.linspace(0, 0.75, 21)
    dPs = p1.deltaP(flows)
    plt.plot(flows, dPs)
    plt.title('Pump Curve - Pressure (psf) vs Flow (cfs)')
    plt.xlabel('Flow')
    plt.ylabel('Pressure at Pump Exit')
    plt.show()

if __name__ == "__main__": 
    main()