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
        tscol, pscol, hfcol, hgcol, sfcol, sgcol, sgcol, vfcol, vgcol = np.loadtxt('sat_water_table.txt', skiprows = 1, unpack = True)

        pval = self.psat

        sfval = float(griddata(pscol, sfcol, pval))
        sgval = float(griddata(pscol, sgcol, pval))
        vfval = float(griddata(pscol, vfcol, pval))
        vgval = float(griddata(pscol, vgcol, pval))
        hfval = float(griddata(pscol, hfcol, pval))
        hgval = float(griddata(pscol, hgcol, pval))
        tsat = float(griddata(pscol, tscol, pval))

        self.tsat = tsat
        self.v = vfval + (vgval - vfval) * self.X
        self.h = hfval + (hgval - hfval) * self.X
        self.s = sfval + (sgval - sfval) * self.X
        

    def display(self):

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
        