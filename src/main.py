import objHandler as objHandler
import bpHandler as bpHandler
import os

user = os.getlogin()
factionsFolder = f"C:\\Users\\{user}\\Documents\\My Games\\Sprocket\\Factions"
if not os.path.exists(factionsFolder):
    factionsFolder = input("Factions folder not found at defualt location, please input here: ")
factions = [name for name in os.listdir(factionsFolder) if os.path.isdir(os.path.join(factionsFolder, name))]
faction = input("Enter faction: ")
while faction not in factions:
    print("Faction not found, please choose from " + str(factions) + ".")
    faction = input("Enter faction: ")

v, f = objHandler.parse_obj(input("Path to .obj file: "))
name = input("Enter compartment name: ")
f = objHandler.correct_edge_ids(f)
e = objHandler.generate_edges(f)
print("Generating Model...")
f = bpHandler.generate_face_info(f)
e = objHandler.delete_duplicate_edges(e)
ef = bpHandler.generate_empty_edge_flags(len(e))
print("Processing Geometry...")
v = bpHandler.combine_all(v)
e = bpHandler.combine_all(e)
print("Combining Data...")

bp = bpHandler.fill_compartment_template(name, v, e, ef, f)

with open(f"{factionsFolder}\\{faction}\\Blueprints\\Plate Structures\\{name}.blueprint", 'w') as file:
    file.write(bp)
    file.close()
print("Done!")
