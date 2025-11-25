# inspiration code for Python Unit Testing Project

import math

def surfaceArea(rad):
    surfaceArea = 4 * math.pi * rad**2
    return surfaceArea

def volume(rad):
    volume = (4/3) * math.pi * rad**3
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))

    print("\nThe surface Area of a Sphere = ", surfaceArea(radius))
    print("\nThe Volume of a Sphere = ", volume(radius))
    
if __name__ == '__main__':
    prompt()
