import json
import sprocketlib as spl
import pywavefront as pwf
import copy

def get_vuid(data: dict, partName: str) -> int:
    """
    Get vuid given part name
    """
    vuid = None
    for bp in data['blueprints']:
        if bp['blueprint']['name'] == partName:
            vuid = bp['blueprint']['bodyMeshVuid']
    
    return vuid

import json

def reformat_vertices(vertices: list) -> list:
    """
    Convert list of sprocketlib.mesh.Vertex objects into a list of coords
    """
    verts = []
    for vert in vertices:
        verts += vert.coords

    return verts

def reformat_faces(faces: list) -> list:
    """
    Convert list of sprocketlib.mesh.Face_IDOnly objects into a list of vertex ids
    """
    return [f.jsonify() for f in faces]

def fill_template(vuid: int, vertices: list, faces: list) -> tuple:
    """
    Fill out compartment template
    """
    template = {
        "vuid":vuid,
        "type":"plateStructureMesh",
        "meshData":{
            "v":"0.0",
            "smoothAngle":0.0,
            "gridSize":1,"format":
            "freeform",
            "mesh":{
                "majorVersion":0,
                "minorVersion":0,
                "vertices": vertices,
                "faces": faces
            }
        }
    }

    return (template, vuid)



def create_scene(filepath: str) -> pwf.Wavefront:
    """
    Create a PyWaveFront Scene
    """
    scene = pwf.Wavefront(
        filepath,
        create_materials=True,
        collect_faces=True,
    )

    return scene

def load_shape_from_obj(data, raw = True):
    if not raw:
        vertices = []
        faces = []
        with open(data) as f:
            for line in f:
                if line[0:2] == "v ":
                    vertex = list(map(float, line[2:].strip().split()))
                    vertices.append(vertex)
                elif line[0] == "f":
                    face = []
                    for i in line[2:].strip().split():
                        face.append(int(i.split('/')[0]))
                    for i in range(len(face)):
                        face[i] = face[i] - 1

                    faces.append(face)

        shape_data = {"vertices": vertices, "faces": faces}

        return shape_data
    else:
        #print(data)
        vertices = []
        faces = []
        for line in data:
            #print(line)
            if line[0:2] == "v ":
                #print("vert")
                vertex = list(map(float, line[2:].strip().split()))
                vertices.append(vertex)
            elif line[0] == "f":
                face = []
                for i in line[2:].strip().split():
                    face.append(int(i.split('/')[0]))
                for i in range(len(face)):
                    face[i] = face[i] - 1

                faces.append(face)

        shape_data = {"vertices": vertices, "faces": faces}

        return shape_data

def populate_vertices(scene: pwf.Wavefront) -> list:
    """
    Create a list of sprocketlib.mesh.Vertex objects
    """
    vertices = []
    index = 0
    for i in scene.vertices:
        vertices.append(spl.mesh.Vertex( i[0] , i[1] ,  i[2] , _id = index))
        index += 1
    
    return vertices

def populate_vertices_alt(scene) -> list:
    """
    Create a list of sprocketlib.mesh.Vertex objects
    """
    vertices = []
    index = 0
    for i in scene["vertices"]:
        #print(i)
        vertices.append(spl.mesh.Vertex( i[0] , i[1] ,  i[2] , _id = index))
        index += 1
    
    return vertices

def populate_faces(scene: pwf.Wavefront, thickness = 1) -> list:
    """
    Create a list of sprocketlib.mesh.Face_IDOnly objects
    """
    # TODO: Switch from Face_IDOnly to Face objects
    faces = []
    for i in scene.mesh_list[0].faces:
        faces.append(spl.mesh.Face_IDOnly(i[0], i[1], i[2], thickness=thickness))
    
    return faces

def populate_faces_alt(scene, thickness = 1) -> list:
    """
    Create a list of sprocketlib.mesh.Face_IDOnly objects
    """
    # TODO: Switch from Face_IDOnly to Face objects
    faces = []
    for i in scene["faces"]:
        try:
            faces.append(spl.mesh.Face_IDOnly(i[0], i[1], i[2], id4 = i[3], thickness=thickness))
        except IndexError:
            faces.append(spl.mesh.Face_IDOnly(i[0], i[1], i[2], thickness=thickness))
    
    return faces

def merge_duplicate_points(v: list, f: list) -> tuple:
    """
    Merge duplicate points
    """
    vertices = copy.deepcopy(v)
    faces = copy.deepcopy(f)

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
    
    # TODO: Remove duplicate points. For some reason, removing points that lack any faces referencing them makes Sprocket freeze

    return (vertices, faces)

def importer(obj: str, compartment: str, vehicle, thickness = 1) -> str:
    """
    Import .obj string as sprocket compartment or into vehicle if asVehicle is specified

    asVehicle should be a string containing data of the file.
    """
    # TODO: implement compartment-only generation
    vData = json.loads(vehicle)
    #print(obj)
    
    scene = load_shape_from_obj(obj, raw=True)
    #print(scene)
    vertices = populate_vertices_alt(scene)
    faces = populate_faces_alt(scene, thickness= thickness)

    vertices, faces = merge_duplicate_points(vertices, faces)

    vertices = reformat_vertices(vertices)
    faces = reformat_faces(faces)

    vuid = get_vuid(vData, compartment)

    template = fill_template(vuid, vertices, faces)[0]

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

    return (vData, 0)

if __name__ == "__main__":
    print(importer()[0])