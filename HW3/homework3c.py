def STO(thrust):
    Vstall = sqrt(56000 / (.5 * .002377 * 1000 *2.4))
    Vto = Vstall * 1.2
    A = 32.2 * (thrust / 56000)
    B = (32.2 / 56000) * (.5 * .002377 * 1000 * .0279)
    
def ThrustNeededForTakeoff(distance):

def main():
    distance = STO(13000)
    print('The take-off distance for an engine with 13,000 pounds of thrust is: {:.1f} feet.'.format(distance))

    thrustNeeded = ThrustNeededForTakeoff(1500)
    print('The thrust needed to take-off in a distance of 1,500 feet is {.2f} pounds.'.format(thrustNeeded))

    thrustNeeded = ThrustNeededForTakeoff(1000)
    print('The thrust needed to take-off in a distance of 1,000 feet is {.2f} pounds.'.format(thrustNeeded))