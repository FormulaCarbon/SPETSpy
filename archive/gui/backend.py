import pywavefront as pwf
from sprocketlib.mesh import *
import json
import os
import getpass

def main(vehiclePath, partName, filepath):

    scene = pwf.Wavefront(
        filepath,
        create_materials=True,
        collect_faces=True,
    )

    """
    print("Faces:", scene.mesh_list[0].faces)
    print("Vertices:", scene.vertices)
    print("Format:", scene.mesh_list[0].materials[0].vertex_format)
    print("Vertices:", scene.mesh_list[0].materials[0].vertices)
    """
    vertices = []
    index = 0
    for i in scene.vertices:
        vertices.append(Vertex(abs(i[0]), abs(i[1]), abs(i[2]), _id = index))
        index += 1

    faces = []
    for i in scene.mesh_list[0].faces:
        faces.append(Face_IDOnly(i[0], i[1], i[2]))

    vData = json.load(open(vehiclePath, 'r'))

    vuid = None

    for bp in vData['blueprints']:
        if bp['blueprint']['name'] == partName:
            vuid = bp['blueprint']['bodyMeshVuid']

    ignore = []
    for vert1 in vertices:
        for vert2 in vertices: 
            if vert1.coords == vert2.coords and vert2 not in ignore:
                for face in faces:
                    if face.vertex_ids[0] == vert2.id:
                        face.vertex_ids[0] = vert1.id
                    if face.vertex_ids[1] == vert2.id:
                        face.vertex_ids[1] = vert1.id
                    if face.vertex_ids[2] == vert2.id:
                        face.vertex_ids[2] = vert1.id
                ignore.append(vert1)
    
    # TODO: remove duplicate points
    #allIDs = []
    #for face in faces:
    #    allIDs += face.vertex_ids
    
    #print(allIDs)

    #for vertex in vertices:
    #    if vertex.id not in allIDs:
    #        vertices.remove(vertex)

                
    
    verts = []
    for vert in vertices:
        verts += vert.coords
    


    template = {
        "vuid":vuid,
        "type":"plateStructureMesh",
        "meshData":{
            "v":"0.0",
            "smoothAngle":0.0,
            "gridSize":1,
            "format":"freeform",
            "mesh":{
                "majorVersion":0,
                "minorVersion":0,
                "vertices":verts,
                "faces": [f.jsonify() for f in faces]
            }
        }
    }

    return (template, vuid)

def get_factions():

    factionsFolder = f"C:/Users/{getpass.getuser()}/OneDrive/Documents/My Games/Sprocket/Factions"
    factions = [name for name in os.listdir(factionsFolder) if os.path.isdir(os.path.join(factionsFolder, name))]

    return factions

def get_vehicles(sender, app_data):
    vehicleFolder = f"C:/Users/{getpass.getuser()}/OneDrive/Documents/My Games/Sprocket/Factions/{app_data}/Blueprints/Vehicles"
    vehicles = [name[:-10] for name in os.listdir(vehicleFolder) if os.path.isfile(os.path.join(vehicleFolder, name)) and os.path.splitext(os.path.join(vehicleFolder, name))[1] == '.blueprint']

    return vehicles
