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
from math import ceil as ceiling

# ---------------------------------------------------
#  Definitions
# ---------------------------------------------------
pumpIndex = -1  # Hardcoding values for the indices for error checking
pipeIndex = -1
bend1Index = -1
bend2Index = -1
turbineIndex = -1
diameterIndex = -1
performanceIndex = -1

g = 9.81  # Acceleration due to gravity in meters per second squared

densityWater = 1000  # Density of water in kilograms per meter cubed

eOut = 120  # Required energy output in MWh

costTotal = 0  # Initial cost of the reservoir is zero dollars

pL = 67.082  # Length of pipe for most efficient pathway in meters

rH = 30  # Elevation of the bottom of the reservoir in meters

bendCoeff1 = 0.15  # The bend loss coefficients of the two 30 degree bends
bendCoeff2 = 0.15

cost = []  # Creates a blank list which will store each of the individual calculated costs
pumpValues = [0.80, 0.83, 0.86, 0.89, 0.92]  # List containing the efficiencies of the 5 pump types
pipeValues = [0.05, 0.03, 0.02, 0.01, 0.005, 0.002]  # List containing the 6 pipe friction values
bendValues = [0.1, 0.15, 0.2, 0.22, 0.27, 0.3]  # List containing the 6 bend loss factors
turbineValues = [0.83, 0.86, 0.89, 0.92, 0.94]  # List containing the efficiencies of the 5 turbine types
performanceRatings = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]  # List containing the performance ratings
# the pumps and turbines
pipeDiameters = [0.1, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]  # List containing the 13 available
# pipe diameters
pump = [[200, 220, 242, 266, 293, 322, 354, 390, 429, 472, 519],
        # List containing the costs for each pump type and performance rating
        [340, 264, 290, 319, 351, 387, 425, 468, 514, 566, 622],
        [240, 364, 290, 319, 351, 387, 425, 368, 514, 566, 622],
        [346, 380, 418, 460, 506, 557, 612, 673, 741, 815, 896],
        [415, 456, 502, 552, 607, 668, 735, 808, 889, 978, 1076]]
pipe = [[1.00, 1.20, 2.57, 6.30, 14, 26, 43, 68, 102, 144, 197, 262, 340],
        # List containing the costs for each pipe type and diameter
        [1.20, 1.44, 3.08, 7.56, 16, 31, 52, 82, 122, 173, 237, 315, 408],
        [1.44, 1.72, 3.70, 9.07, 20, 37, 63, 98, 146, 208, 284, 378, 490],
        [2.16, 2.8, 5.55, 14, 29, 55, 94, 148, 219, 311, 426, 567, 735],
        [2.70, 3.23, 6.94, 17, 37, 69, 117, 185, 374, 389, 533, 708, 919],
        [2.97, 3.55, 7.64, 19, 40, 76, 129, 203, 302, 428, 586, 339, 1011]]
bend = [[1.00, 1.49, 4.93, 14, 32, 62, 107, 169, 252, 359, 492, 654, 849],  # List containing the costs for each bend
        # angle and pipe diameter
        [1.05, 1.57, 5.17, 15, 34, 65, 112, 178, 265, 377, 516, 687, 892],
        [1.10, 1.64, 5.43, 16, 36, 69, 118, 187, 278, 396, 542, 721, 936],
        [1.16, 1.73, 5.70, 16, 38, 72, 124, 196, 292, 415, 569, 757, 983],
        [1.22, 1.81, 5.99, 17, 39, 76, 130, 206, 307, 436, 598, 795, 1032],
        [1.28, 1.90, 7, 18, 41, 80, 137, 216, 322, 458, 628, 835, 1084]]
turbine = [[360, 396, 436, 479, 527, 580, 638, 702, 772, 849, 934],  # List containing the costs for each turbine type
           # and performance rating
           [432, 475, 523, 575, 632, 696, 765, 842, 926, 1019, 1120],
           [518, 570, 627, 690, 759, 835, 918, 1010, 1111, 1222, 1345],
           [622, 684, 753, 828, 911, 1002, 1102, 1212, 1333, 1467, 1614],
           [746, 821, 903, 994, 1093, 1202, 1322, 1455, 1600, 1760, 1936]]


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


def energyreq(m, h, f, l, v, d, k1, k2, np):  # Determines the energy input required for a given energy output
    # and given system characteristics
    ein = (m * (g * h + ((f * l * (v ** 2)) / (2 * d)) + ((k1 * (v ** 2)) / 2) + ((k2 * (v ** 2)) / 2))) / np
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


def reservoirsidelength(a):  # Determines the reservoir side length required for a given reservoir area
    d = sqrt(a)
    return d


def reservoirperimeter(d):  # Determines the reservoir perimeter required for a give reservoir diameter
    p = 4 * d
    return p


def wallc(resd, p):  # Determines the cost per meter of reservoir wall for a given reservoir depth using
    # linear regression
    wc = (30 + (resd - 5) * (340 - 30) / (20 - 5)) * ceiling(p)
    return wc


def pipec(p, d, l):  # Determines the cost of the total length of pipe required for a given pipe
    # type, diameter, and length
    pc = pipe[p][d] * ceiling(l)
    return pc


def bendc(b, d):  # Determines the cost of a bend given a bend type and diameter
    bc = bend[b][d]
    return bc


def pumpc(p, pfi, q):  # Determines the cost of the pump for a given pump type, performance rating, and flow rate
    pc = pump[p][pfi] * q
    return pc


def turbinec(t, pfi, q):  # Determines the cost of the turbine for a given turbine type, performance rating,
    # and flow rate
    tc = turbine[t][pfi] * q
    return tc


def pipeintstallc(l):  # Determines the cost of installing the total length of pipe required
    pic = 500 * ceiling(l)
    return pic


def siteprepc(a):  # Determines the cost of preparing the land required for the reservoir given the reservoir area
    spc = 0.25 * ceiling(a)
    return spc


# ---------------------------------------------------
#  Inputs
# ---------------------------------------------------
print("Type : Efficiency \n Cheap : 0.80 \n Value : 0.83 \n Standard : 0.86 \n High-Grade 0.89 \n Premium : 0.92")
pEff = float(input("Enter the pump efficiency: "))
pFlowRate = float(input("Enter the pump volumetric flow rate in cubic meters per second: "))
pDiameter = float(input("Enter the pipe diameter in meters: "))
# pL = float(input("Enter the pipe length in meters: "))
print("Type : Friction Coefficient \n Salvage : 0.05 \n Questionable : 0.03 \n Better : 0.02 \n Nice : 0.01 \n"
      " Outstanding : 0.005 \n Glorious 0.002")
pFCoeff = float(input("Enter the pipe friction coefficient: "))
rDepth = float(input("Enter the reservoir depth in meters: "))
# rH = float(input("Enter the elevation of the bottom of the reservoir in meters: "))
# print("Angle : Loss Coefficient \n 20 : 0.1\n 30 : 0.15 \n 45 : 0.2 \n 60 : 0.22 \n 75 : 0.27 \n 90 : 0.3")
# bendCoeff1 = float(input("Enter the bend coefficient of bend #1: "))
# bendCoeff2 = float(input("Enter the bend coefficient of bend #2: "))
print("Type : Efficiency \n Meh : 0.83 \n Good : 0.86 \n Fine : 0.89 \n Super 0.92 \n Mondo : 0.94")
tEff = float(input("Enter the turbine efficiency: "))
tFlowRate = float(input("Enter the turbine volumetric flow rate in cubic meters per second: "))
# ---------------------------------------------------
#  Categorizing inputs
# ---------------------------------------------------
for i in range(len(pumpValues)):
    if pEff == pumpValues[i]:
        pumpIndex = i
        print(pumpIndex)

for i in range(len(pipeValues)):
    if pFCoeff == pipeValues[i]:
        pipeIndex = i
        print(pipeIndex)

for i in range(len(bendValues)):
    if bendCoeff1 == bendValues[i]:
        bend1Index = i
        print(bend1Index)

for i in range(len(bendValues)):
    if bendCoeff2 == bendValues[i]:
        bend2Index = i
        print(bend2Index)

for i in range(len(turbineValues)):
    if tEff == turbineValues[i]:
        turbineIndex = i
        print(turbineIndex)

for i in range(len(pipeDiameters)):
    if pDiameter == pipeDiameters[i]:
        diameterIndex = i
        print(diameterIndex)

for i in range(len(performanceRatings)):
    if ceiling((rH + rDepth) / 10) * 10 == performanceRatings[i]:
        performanceIndex = i
        print(performanceIndex)

# ---------------------------------------------------
#  Computations
# ---------------------------------------------------
pArea = pipearea(pDiameter)
vUp = velocity(pFlowRate, pArea)
vDown = velocity(tFlowRate, pArea)
effH = effelevation(rH, rDepth)
eOutJ = mwhtojoule(eOut)
waterMass = massreq(eOutJ, tEff, effH, pFCoeff, pL, vDown, pDiameter, bendCoeff1, bendCoeff2)
eInJ = energyreq(waterMass, effH, pFCoeff, pL, vUp, pDiameter, bendCoeff1, bendCoeff2, pEff)
rArea = reservoirarea(eOutJ, tEff, waterMass, pFCoeff, pL, vDown, pDiameter,
                      bendCoeff1, bendCoeff2, densityWater, rDepth, effH)
tFill = timereq(pFlowRate, waterMass)
tEmpty = timereq(tFlowRate, waterMass)
eIn = jouletomwh(eInJ)
nsys = syseff(eOut, eIn)
rSide = reservoirsidelength(rArea)
rPerim = reservoirperimeter(rSide)
# ---------------------------------------------------
#  Cost Summation
# ---------------------------------------------------
cost.append(wallc(rDepth, rPerim))
cost.append(pipec(pipeIndex, diameterIndex, pL))
cost.append(bendc(bend1Index, diameterIndex))
cost.append(bendc(bend2Index, diameterIndex))
cost.append(pumpc(pumpIndex, performanceIndex, pFlowRate))
cost.append(turbinec(turbineIndex, performanceIndex, tFlowRate))
cost.append(pipeintstallc(pL))
cost.append(siteprepc(rArea))
cost.append(100000)
cost.append(40000)
cost.append(10000)

for i in range(len(cost)):
    costTotal = costTotal + cost[i]

# ---------------------------------------------------
#  Outputs
# ---------------------------------------------------
if rSide <= 600:
    if pumpIndex == -1 or pipeIndex == -1 or bend1Index == -1 or bend2Index == -1 or turbineIndex == -1 or diameterIndex\
                 == -1 or performanceIndex == -1:
        print("Invalid input paramters, input data does not match part sheet")
    else:
        print()
        print("Required mass of water in kilograms: ", waterMass, " kilograms", sep="")
        print("Required energy input: ", eIn, " MWh", sep="")
        print("Efficiency of system: ", eOut / eIn, sep="")
        print("Required surface area of reservoir: ", rArea, " square meters", sep="")
        print("Time to fill: ", tFill, " hours", sep="")
        print("Time to empty: ", tEmpty, " hours", sep="")
        print("Cost to build reservoir: $", round(costTotal, 2), sep="")

else:
    print()
    print("Invalid input parameters, reservoir is too large")
