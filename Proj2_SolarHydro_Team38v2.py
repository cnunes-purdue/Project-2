# Project 2: Solar Hydro Plant.
# File: Proj2_SolarHydro_Team38.py
# Date: 28 October 2019
# By: Cohen Thomas Vestal Nunes
# cnunes
# Full Name team member 2
# Login ID
# Full Name team member 3
# Login ID
# Full Name team member 4
# Login ID
# Section: 3
# Team: 38
#
# ELECTRONIC SIGNATURE
# Cohen Thomas Vestal Nunes
# Full Name team member 2
# Full Name team member 3
# Full Name team member 4
#
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an
# equal participant in its creation. In addition, each
# member of the team has a general understanding of
# all aspects of the program development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE PROGRAM OR FUNCTION DOES
#       Computes the mass of water, input energy, time to fill, and time to empty requirements for the
#       Solar Hydro Plant as well as the overall efficiency of the system for Zone 3
# ---------------------------------------------------
#  Imports
# ---------------------------------------------------
from math import pi as pi
from math import sqrt as sqrt

# ---------------------------------------------------
#  Definitions
# ---------------------------------------------------
g = 9.81  # Acceleration due to gravity in meters per second squared

densityWater = 1000  # Density of water in kilograms per meter cubed

eOut = 120  # Required energy output in MWh

pumpCheap = [200, 220, 242, 266, 293, 322, 354, 390, 429, 472, 519]
pumpValue = [340, 264, 290, 319, 351, 387, 425, 468, 514, 566, 622]
pumpStandard = [240, 364, 290, 319, 351, 387, 425, 368, 514, 566, 622]
pumpHighGrade = [346, 380, 418, 460, 506, 557, 612, 673, 741, 815, 896]
pumpPremium = [415, 456, 502, 552, 607, 668, 735, 808, 889, 978, 1076]
pipeSalvage = [1.00, 1.20, 2.57, 6.30, 14, 26, 43, 68, 102, 144, 197, 262, 340]
pipeQuestionable = [1.20, 1.44, 3.08, 7.56, 16, 31, 52, 82, 122, 173, 237, 315, 408]
pipeBetter = [1.44, 1.72, 3.70, 9.07, 20, 37, 63, 98, 146, 208, 284, 378, 490]
pipeNice = [2.16, 2.8, 5.55, 14, 29, 55, 94, 148, 219, 311, 426, 567, 735]
pipeOutstanding = [2.70, 3.23, 6.94, 17, 37, 69, 117, 185, 374, 389, 533, 708, 919]
pipeGlorious = [2.97, 3.55, 7.64, 19, 40, 76, 129, 203, 302, 428, 586, 339, 1011]
bend20 = [1.00,1.49,4.93,14,32,62,107,169,252,359,492,654,849]
bend30 = [1.05,1.57,5.17,15,34,65,112,178,265,377,516,687,892]
bend45 = [1.10,1.64,5.43,16,36,69,118,187,278,396,542,721,936]
bend60 = [1.16,1.73,5.70,16,38,72,124,196,292,415,569,757,983]
bend75 = [1.22,1.81,5.99,17,39,76,130,206,307,436,598,795,1032]
bend90 = [1.28,1.90,7,18,41,80,137,216,322,458,628,835,1084]
turbineMeh = [360,396,436,479,527,580,638,702,772,849,934]
turbineGood = [432,475,523,575,632,696,765,842,926,1019,1120]
turbineFine = [518,570,627,690,759,835,918,1010,1111,1222,1345]
turbineSuper = [622,684,753,828,911,1002,1102,1212,1333,1467,1614]
turbuneMondo = [746,821,903,994,1093,1202,1322,1455,1600,1760,1936]


def pipearea(d):  # Determines the cross-sectional area of the pipe
    pipea = pi * ((d / 2) ** 2)
    return pipea


def velocity(q, a):  # Determines the velocity of the water give the area of the pipe and the volumetric flow rate
    # of the pump/turbine
    v = q / a
    return v


def effelevation(h, depth):  # Determines the effective elevation of the reservoir
    eh = h + (depth / 2)
    return eh


def mwhtojoule(e):  # Converts MWh to joules
    j = e * 3.6E9
    return j


def jouletomwh(e):  # Converts joules to MWh
    w = e / 3.6E9
    return w


def massreq(e, nt, h, f, l, v, d, k1, k2):  # Determines the mass required for a given energy output
    # and given system characteristics
    m = (e * (1 / nt)) / (g * h - ((f * l * (v ** 2)) / (2 * d)) - ((k1 * (v ** 2)) / 2) - ((k2 * (v ** 2)) / 2))
    return m


def energyreq(m, h, f, l, v, d, k1, k2, nt):  # Determines the energy input required for a given energy output
    # and given system characteristics
    ein = (m * (g * h + ((f * l * (v ** 2)) / (2 * d)) + ((k1 * (v ** 2)) / 2) + ((k2 * (v ** 2)) / 2))) / nt
    return ein


def reservoirarea(e, nt, m, f, l, v, d, k1, k2, rho, depth, h):  # Determines the reservoir area required for a
    # given mass of water and given system characteristics
    a = (e * (1 / nt) + m * ((f * l * (v ** 2)) / (2 * d)) + ((k1 * (v ** 2)) / 2) + ((k2 * (v ** 2)) / 2)) / \
        (rho * depth * g * h)
    return a


def syseff(eout, ein):  # Determines the system efficiency
    ns = eout / ein
    return ns


def timereq(q, m):  # Determines the time, in hours, to fill/empty for a given volumetric flow rate
    # and given system characteristics
    t = (m / (densityWater * q)) / 3600
    return t


def reservoirdiameter(a):  # Determines the reservoir diameter required for a given reservoir area
    d = sqrt((4 * a) / pi)
    return d

def reservoirperimeter(d): # Determines the reservoir perimeter required for a give reservoir diameter
    p = pi * d
    return p

def wallcost(resd):
    wallc = 30 + (resd - 5)*(340 - 30)/(20 - 5)
    return wallc


# ---------------------------------------------------
#  Inputs
# ---------------------------------------------------
pEff = float(input("Enter the pump efficiency: "))
pFlowRate = float(input("Enter the pump volumetric flow rate in cubic meters per second: "))
pDiameter = float(input("Enter the pipe diameter in meters: "))
pL = float(input("Enter the pipe length in meters: "))
pFCoeff = float(input("Enter the pipe friction coefficient: "))
rDepth = float(input("Enter the reservoir depth in meters: "))
rH = float(input("Enter the elevation of the bottom of the reservoir in meters: "))
bendCoeff1 = float(input("Enter the bend coefficient of bend #1: "))
bendCoeff2 = float(input("Enter the bend coefficient of bend #2: "))
tEff = float(input("Enter the turbine efficiency: "))
tFlowRate = float(input("Enter the turbine volumetric flow rate in cubic meters per second: "))

# ---------------------------------------------------
#  Computations
# ---------------------------------------------------
pArea = pipearea(pDiameter)
vUp = velocity(pFlowRate, pArea)
vDown = velocity(tFlowRate, pArea)
effH = effelevation(rH, rDepth)
eOutJ = mwhtojoule(eOut)
waterMass = massreq(eOutJ, tEff, effH, pFCoeff, pL, vDown, pDiameter, bendCoeff1, bendCoeff2)
eInJ = energyreq(waterMass, effH, pFCoeff, pL, vUp, pDiameter, bendCoeff1, bendCoeff2, tEff)
rArea = reservoirarea(eOutJ, tEff, waterMass, pFCoeff, pL, vDown, pDiameter,
                      bendCoeff1, bendCoeff2, densityWater, rDepth, effH)
tFill = timereq(pFlowRate, waterMass)
tEmpty = timereq(tFlowRate, waterMass)
eIn = jouletomwh(eInJ)
nsys = syseff(eOut, eIn)
rDiam = reservoirdiameter(rArea)

# ---------------------------------------------------
#  Outputs
# ---------------------------------------------------
if rDiam < (450 / sqrt(5)):
    print()
    print("Required mass of water in kilograms: ", waterMass)
    print("Required energy input in MWh: ", eIn)
    print("Efficiency of system", eOut / eIn)
    print("Required surface area of reservoir: ", rArea)
    print("Time to fill: ", tFill)
    print("Time to empty: ", tEmpty)
else:
    print()
    print("Invalid input parameters, reservoir is too large")
