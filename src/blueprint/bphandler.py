import copy

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

def get_vuid(data: dict, partName: str) -> int:
    """
    Get vuid given part name
    """
    vuid = None
    for bp in data['blueprints']:
        if bp['blueprint']['name'] == partName:
            vuid = bp['blueprint']['bodyMeshVuid']
    
    return vuid