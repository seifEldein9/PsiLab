
from math import*
#mechanics physics

#Speed calculation
def velocity(distance,time):
    return distance/time
#time calculation 
def time(distance,velocity):
    return distance/velocity
#Distance calculation
def distance(velocity,time):
    return velocity*time
#Calculating acceleratio
def acceleration(velocity,time):   
    return velocity/time
#volume
def volume(length,Height,width):   
    return length*Height*width
#density
def density(mass,volume):
    return mass/volume
#force
def force(mass,acceleration):
    return mass*acceleration
#work
def work(force,distance):
    return force*distance
#work with cos theta
def workTheta(force,distance,theta):
    return force*distance*cos(theta)
#The resultant of two forces between them is theta
def resultantOftwoForces(force1,force2,theta):
    return sqrt(pow(force1,2)+pow(force2,2)+2*force1*force2*cos(theta))
#The direction of the resultant force between two forces is theta angle
def directionOfTheResultant(force1,force2,theta):
    return atan((force2*sin(theta))/(force1+force2*cos(theta)))
#Force analysis in two orthogonal directions
def forceAnalysisInTwoOrthogonalDirections(force,theta):
    fx = force*cos(theta)
    Rx =  fx
    fy = force*sin(theta)
    Ry =  fy
    return sqrt(pow(Rx,2)+pow(Ry,2))
#The direction of the resultant two-force analysis
def directionOfTheResultantTwoForce(Rx,Ry):
    return atan((Ry)/(Rx))
#gravitational constant
def g():
    return 9.8
#linear distance
def linearDistance(velocity,time,acceleration):
    return (velocity*time+(1/2)*acceleration*pow(time,2))
#linear time
def linearTime(velocity,initialvelocity,acceleration):
    return (initialvelocity-velocity)/(acceleration)
#circular time
def circularTime(theta,Omega):
    return (theta)/(Omega)
#periodic displacement
def periodicDisplacement(Omega,time):
    return (Omega)*(time)
#periodic speed
def omega(theta,time):
    return (theta)/(time)
#frequency
def frequency(Omega):
    return (Omega)/(2*3.141592654)
#Angular velocity
def angularVelocity(theta,time,frequency):
    return (theta)/(time)*((2*3.141592654)*frequency)
#linear wheel
def linearAcceleration(Omega,time):
    return (Omega)/(time)
#tangential velocity
def tangentialVelocity(Omega,length):
    return (Omega)*(length)
#torque 
def torque(force,length):
    return (force)*(length)
#torque with theta
def torqueWithTheta(force,length,theta):
    return (force)*(length)*sin(theta)
#Friction force
def frictionforce(u,fn):
    return (u)*(fn)
#friction coefficient
def frictionCoefficient(Ff,fn):
    return (Ff)/(fn)
#gravitational force
def gravitationalForce(Mass):
    return (Mass)*(9.80665)
#The general law of attraction
def generalLawOfAttraction(Mass1,Mass2,length):
    return (6.67428*pow(10,-11))*((Mass1*Mass2)/(pow(length,2)))
#Kinetic energy
def kineticEnergy(Mass,velocity):
    return (1/2)*(Mass)*pow(velocity,2)
#Energy situation
def energySituation(work,length):
    return (work)*(length)
#HookeIsLaw
def hookeIsLaw(k,x):
    return -(k)*(x)
#periodic time
def periodicTime(Omega):
    return (2*(3.141592654))/(Omega)
#Power
def power(work,time):
    return (work)/(time)
#Conversion from horsepower to joules
def conversionFromHorsepowerToJoules(hp):
    return (hp)*(735)
#Graphic ability
def graphicAbility(fp,Bp):
    return (fp)+(Bp)
#####################################
#Electrical and magnetic physics
####################################
#A coulomb is equal to how many electrons
def coulombIsEqualToHowManyElectrons(coulomb):
    return (coulomb)*(6.25*pow(10,18))
#Electrons equal to the number of coulombs
def electronsEqualToTheNumberOfCoulombs(electrons):
    return (electrons)*(1.6*pow(10,-19))
#The work done to move the electric charge
def electricWork(coulomb,volt):
    return (coulomb)*(volt)
#coulomb
def coulomb(work,volt):
    return (work)/(volt)
#current
def current(volt,resistance):
    return (volt)/(resistance)
#Electrical Power
def electricalPower(volt,current):
    return (volt)*(current)
#volt
def volt(current,resistance):
    return (current)*(resistance)
#resistance
def resistance(volt,current):
    return (volt)/(current)
#electrical resistance of the conductor
def conductorResistance(conductiveMaterial,height,area):
    return (conductiveMaterial)*((height)/(area))
#Conductor material type
def conductorMaterialType(resistance,height,area):
    return (resistance)*((area)/(height))
#electrical conductivity
def electricalConductivity(conductorMaterialType):
    return 1/(conductorMaterialType)
#the magnetic field
def magneticField(magneticFlux,area):
    return (magneticFlux)/(area)
#magneticFlux
def magneticFlux(magneticField,area):
    return (magneticField)*(area)
#magnetic flux area
def magneticFluxArea(magneticFlux,magneticField):
    return (magneticFlux)/(magneticField)
#magnetic flux density
def magneticFluxDensity(current,numberOfTurns,magneticPermeability,RadiusLength):
    return (magneticPermeability*numberOfTurns*current)/(2*RadiusLength)
#magnetic field force
def magneticFieldForce(magneticField,current,height):
    return (magneticField)*(current)*(height)
#Magnetic field strength with theta
def magneticFieldForceWithTheta(magneticField,current,height,theta):
    return (magneticField)*(current)*(height)*(sin(theta))
#flux density
def fluxDensity(magneticFieldForce,current,height,theta):
    return (magneticFieldForce)/((current)*(height)*(sin(theta)))
#magnetic moment
def magneticMoment(current,area,numberOfTurns):
    return (current)*(area)*(numberOfTurns)
#The average electromotive force generated by a charged coil
def averageElectromotiveForceGeneratedByAChargedCoil(magneticFlux,time,numberOfTurns):
    return (-numberOfTurns)*((magneticFlux)/(time))
#mutual induction
def mutualInduction(factorAffectingTheInductanceCoefficient,current,time):
    return (-factorAffectingTheInductanceCoefficient)*((current)/(time))
#factorAffectingTheInductanceCoefficient
def factorAffectingTheInductanceCoefficient(mutualInduction,current,time):
    return (mutualInduction)/((current)/(time))
#capacitor capacitance
def capacitorCapacitance(coulomb,volt):
    return (coulomb)/(volt)
#capacitor charge
def capacitorCharge(absoluteInsulationConstant,plateSpace,TheDistanceBetweenThePanels):
    return (absoluteInsulationConstant)*(plateSpace)/(TheDistanceBetweenThePanels)
#wave speed
def waveSpeed(frequencie,waveLength):
    return (frequencie)*(waveLength)
#Convert temperature from Celsius to Kelvin
def ConvertTemperatureFromCelsiusToKelvin(Celsius):
    return (Celsius)+(273)
#Finn Is law
def FinnIslaw(KelvinTemperature):
    return (2.898*pow(10,-3))/(KelvinTemperature)
#bulb filament temperature
def bulbFilamentTemperature(FinnIslaw):
    return (2.898*pow(10,-3))/(FinnIslaw)
#photon energy
def photonEnergy(frequencie):
    return (6.625*pow(10,-34))*(frequencie)
#Planck's constant
def PlanckIsConstant():
    return (6.625*pow(10,-34))
#Conversion from electron volts to joules
def conversionFromElectronVoltsToJoules(ElectronVolts):
    return (ElectronVolts)*(1.6*pow(10,-19))
#Conversion from joules to electron volts
def conversionFromJoulesToElectronVolts(joules):
    return (joules)*(1.25*pow(10,18))
#electron volt
def electronVolt(mass,velocity):
    return (1/2)*(mass*pow(velocity,2))
#futon speed
def futonSpeed(mass,energy):
    return (sqrt(energy/mass))
#Law of conservation of mass and energy
def LawOfConservationOfMassAndEnergy(mass,TheSpeedOfLight):
    return (mass*pow(TheSpeedOfLight,2))
#photon momentum
def photonMomentum(mass,TheSpeedOfLight):
    return (mass)*(TheSpeedOfLight)
#Photon energy in motion
def PhotonEnergyInMotion(Energy,TheSpeedOfLight):
    return (Energy)/(pow(TheSpeedOfLight,2))
#wave length
def waveLength(PhotonEnergyInMotion):
    return (6.625*pow(10,-34))/(PhotonEnergyInMotion)
#Coulomb's law
def CoulombIsLaw(Coulomb1,Coulomb2,length):
    return (8.9875517873681764*pow(10,9))*((Coulomb1*Coulomb2)/(pow(length,2)))
