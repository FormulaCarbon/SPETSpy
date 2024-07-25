from SPETS import importer
import time

objpath = input("Path to .obj file: ")
compartment = input("Compartment name: ")
faction = input("Faction: ")
vehicle = input("Vehicle: ")

time.sleep(5)

print(importer(objpath, compartment, asVehicle = f"{faction}.{vehicle}")[0])