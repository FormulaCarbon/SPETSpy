from SPETS import importer

objpath = input("Path to .obj file: ")
compartment = input("Compartment name: ")
faction = input("Faction: ")
vehicle = input("Vehicle: ")

print(importer(objpath, compartment, asVehicle = f"{faction}.{vehicle}")[0])