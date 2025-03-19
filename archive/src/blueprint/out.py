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
