import json
import getpass
import os
import backend

FACTIONSFOLDER = f"C:/Users/{getpass.getuser()}/OneDrive/Documents/My Games/Sprocket/Factions"

FACTIONS = [name for name in os.listdir(FACTIONSFOLDER) if os.path.isdir(os.path.join(FACTIONSFOLDER, name))]

faction = None
while faction not in FACTIONS:
    faction = input("Faction: ")
    if faction not in FACTIONS:
        print("Faction not found, please choose from " + str(FACTIONS))

vehicleFolder = FACTIONSFOLDER + f'/{faction}/Blueprints/Vehicles'
vehicles = [name[:-10] for name in os.listdir(vehicleFolder) if os.path.isfile(os.path.join(vehicleFolder, name)) and os.path.splitext(os.path.join(vehicleFolder, name))[1] == '.blueprint']

vehicle = None
while vehicle not in vehicles:
    vehicle = input("Vehicle: ")
    if vehicle not in vehicles:
        print("Vehicle not found, please choose from " + str(vehicles))
    
vehicle += '.blueprint'

compartment = input("Name of addon compartment: ")

out, vuid = backend.main(vehicleFolder + '/' + vehicle, compartment)

out = {
    'meshes': [out]
}

vData = json.load(open(vehicleFolder + '/' + vehicle, 'r'))

for mesh in vData['meshes']:
    if mesh['vuid'] == vuid:
        mesh['meshData']['mesh'] = out['meshes'][0]['meshData']['mesh']

with open(vehicleFolder + '/' + vehicle, 'w') as vFile:
    json.dump(vData, vFile)
    vFile.close()

print("Done!")