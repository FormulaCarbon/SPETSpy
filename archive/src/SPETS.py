import blueprint.bphandler as bphandler
import blueprint.filehandler as filehandler
import blueprint.out as out

import mesh.objhandler as objhandler

import typer
import json
import os

app = typer.Typer()

@app.command()
def importer(objpath: str, compartment: str, asVehicle: str = "" ):
    """
    Import .obj file as sprocket compartment or into vehicle if --asVehicle is specified

    if --asVehicle is specified, then put faction and vehicle in the format "Faction.Vehicle", including quotes
    """
    # TODO: implement compartment-only generation
    if asVehicle != "":
        factionsFolder = filehandler.get_factions_folder()
        # TODO: Implement proper fix
        if not os.path.exists(factionsFolder):
            err = 4
            print("Faction folder not found at " + factionsFolder + f". Please enter path below.")
            factionsFolder = input(" Folder containing Factions: ")
        factions = filehandler.get_factions(factionsFolder)

        faction, vehicle = asVehicle.split(".")

        if faction not in factions:
            err = 1
            return ("Faction not found, please choose from " + str(factions) + f". Aborting with error code {err}.", err)
        
        vehiclesFolder = filehandler.get_vehicles_folder(factionsFolder, faction)
        vehicles = filehandler.get_vehicles(vehiclesFolder)

        if vehicle not in vehicle:
            err = 2
            return ("Vehicle not found, please choose from " + str(vehicles) + f". Aborting with error code {err}.", err)
        
        #scene = objhandler.create_scene(objpath)
        #vertices = objhandler.populate_vertices(scene)
        #faces = objhandler.populate_faces(scene)
        scene = objhandler.load_shape_from_obj(objpath, raw=False)
        vertices = objhandler.populate_vertices_alt(scene)
        faces = objhandler.populate_faces_alt(scene)
        

        # TODO: Properly get full vehicle path
        vData = filehandler.load_bp_as_dict(vehiclesFolder + "/" + vehicle + ".blueprint")

        vertices, faces = objhandler.merge_duplicate_points(vertices, faces)

        vertices = out.reformat_vertices(vertices)
        faces = out.reformat_faces(faces)

        #print(vertices)
        #print(faces)

        vuid = bphandler.get_vuid(vData, compartment)

        template = out.fill_template(vuid, vertices, faces)[0]

        cData = {
            'meshes': [template]
        }

        found = False
        for mesh in vData['meshes']:
            if mesh['vuid'] == vuid:
                mesh['meshData']['mesh'] = cData['meshes'][0]['meshData']['mesh']
                found = True
                
        if not found:
            err = 3
            return (f"Compartment {compartment} not found. Aborting with error code {err}.", err)
        
        with open(vehiclesFolder + '/' + vehicle + '.blueprint', 'w') as vFile:
            json.dump(vData, vFile)
            vFile.close()

        return ("Completed", 0)

if __name__ == "__main__":
    app()