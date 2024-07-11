import pywavefront as pwf
import sprocketlib as spl
import copy

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

def populate_faces(scene: pwf.Wavefront) -> list:
    """
    Create a list of sprocketlib.mesh.Face_IDOnly objects
    """
    # TODO: Switch from Face_IDOnly to Face objects
    faces = []
    for i in scene.mesh_list[0].faces:
        faces.append(spl.mesh.Face_IDOnly(i[0], i[1], i[2]))
    
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
