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
#       Solar Hydro Plant as well as the overall efficiency of the system
# ---------------------------------------------------
#  Imports
# ---------------------------------------------------
from math import pi as pi

# ---------------------------------------------------
#  Definitions
# ---------------------------------------------------
g = 9.81  # Acceleration due to gravity in meters per second squared

densityWater = 1000  # Density of water in kilograms per meter cubed

eOut = 120  # Required energy output in MWh


def pipearea(d):  # Determines the cross-sectional area of the pipe
    pipeA = pi * ((d / 2) ** 2)
    return pipeA


def velocity(q, a):  # Determines the velocity of the water give the area of the pipe and the volumetric flow rate
    # of the pump/turbine
    v = q / a
    return v


def effelevation(h, depth):  # Determines the effective elevation of the reservoir
    H = h + (depth / 2)
    return H


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
    ein = (m * (g * h + ((f * l * (v ** 2)) / (2 * d)) + ((k1 * (v ** 2)) / 2) + ((k2 * (v ** 2)) / 2)))/nt
    return ein


def reservoirarea(e, nt, m, f, l, v, d, k1, k2, rho, depth, h):  # Determines the reservoir area required for a
    # given mass of water and given system characteristics
    a = (e * (1 / nt) + m * ((f * l * (v ** 2)) / (2 * d)) + ((k1 * (v ** 2)) / 2) + ((k2 * (v ** 2)) / 2)) / (
                rho * depth * g * h)
    return a


def syseff(eout, ein):  # Determines the system efficiency
    ns = eout / ein
    return ns


def timereq(q, m):  # Determines the time, in hours, to fill/empty for a given volumetric flow rate
    # and given system characteristics
    t = (m / (densityWater * q)) / 3600
    return t


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
# ---------------------------------------------------
#  Outputs
# ---------------------------------------------------
print("Required mass of water in kilograms: ", waterMass)
print("Required energy input in MWh: ", eIn)
print("Efficiency of system J", (eOutJ / eInJ) * 100)
print("Efficiency of system MWh", (eOut / eIn) * 100)
print("Required surface area of reservoir: ", rArea)
print("Time to fill: ", tFill)
print("Time to empty: ", tEmpty)
