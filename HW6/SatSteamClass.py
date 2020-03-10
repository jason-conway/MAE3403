from scipy.interpolate import griddata
import numpy as np

class SatSteam:
    def __init__(self, psat, quality = None, name = None):
        self.psat = psat
        self.X = quality
        self.name = name
        self.tsat = None
        self.h = None
        self.s = None
        self.v = None
        if self.X is not None: #Quality was given so update the other properties
            self.updateProperties()

    #Set the quality value and update the properties
    def Quality(self, quality):
        self.X = quality
        self.updateProperties()

    def updateProperties(self):
        rawSatTemp, rawSatPressure, rawSatFluidEnthalpy, rawSatVaporEnthalpy, rawSatFluidEnthropy, rawSatVaporEnthropy, rawSatFluidSpecificVolume, rawSatVaporSpecificVolume = np.loadtxt("sat_water_table.txt", skiprows = 1, unpack = True) #Load the text file and unpack the contents into their respective variables 

        satFluidEnthropy = float(griddata(rawSatPressure, rawSatFluidEnthropy, self.psat)) #Interpolate the saturated fluid entropy
        satVaporEnthropy = float(griddata(rawSatPressure, rawSatVaporEnthropy, self.psat)) #Interpolate the saturated vapor entropy
        satFluidSpecificVolume = float(griddata(rawSatPressure, rawSatFluidSpecificVolume, self.psat)) #Interpolate the saturated fluid specific volume
        satVaporSpecificVolume = float(griddata(rawSatPressure, rawSatVaporSpecificVolume, self.psat)) #Interpolate the saturated vapor specific volume
        satFluidEnthalpy = float(griddata(rawSatPressure, rawSatFluidEnthalpy, self.psat)) #Interpolate the saturated fluid enthalpy
        satVaporEnthalpy = float(griddata(rawSatPressure, rawSatVaporEnthalpy, self.psat))  #Interpolate the saturated vapor enthalpy
        satTemp = float(griddata(rawSatPressure, rawSatTemp, self.psat))  #Interpolate the saturation temperature

        self.tsat = satTemp #Update saturation temp internally
        self.v = satFluidSpecificVolume + (satVaporSpecificVolume - satFluidSpecificVolume) * self.X #Find the specific volume using the provided quality
        self.h = satFluidEnthalpy + (satVaporEnthalpy - satFluidEnthalpy) * self.X #Find the enthalpy using the provided quality
        self.s = satFluidEnthropy + (satVaporEnthropy - satFluidEnthropy) * self.X #Find the entropy using the provided quality

        return None

    def display(self):
        if self.name != None: print('Name: {}'.format(self.name)) #Print out the name as long as it isn't None
        if self.psat != None: print('Saturation Pressure is {:.2f} kPa'.format(self.psat)) #Print out the saturation pressure as long as it isn't None
        if self.tsat != None: print('Saturation Temperature is {:.2f} C'.format(self.tsat)) #Print out the name as long as it isn't None
        if self.h != None: print('Entropy is {:.2f} kJ/kg'.format(self.h)) #Print out the entropy as long as it isn't None
        if self.s != None: print('Enthalpy is {:.2f} kJ/kg*K'.format(self.s)) #Print out the enthalpy as long as it isn't None
        if self.v != None: print('Specific Volume is {:.5f} m^3/kg'.format(self.v)) #Print out the specific volumne as long as it isn't None
        if self.X != None: print('Quality is {:.4f}\n'.format(self.X)) #Print out the quality as long as it isn't None

def main():
    state1 = SatSteam(90, quality = 1.00, name = 'Turbine Inlet')
    state1.display()

    state2 = SatSteam(8, name = 'Turbine Exit')
    state2.Quality(0.7874)
    state2.display()

    state3 = SatSteam(8, quality = 0.0) #No name
    state3.display()

if __name__ == "__main__": 
    main()
        