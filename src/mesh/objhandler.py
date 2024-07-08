import pywavefront as pwf
import sprocketlib as spl

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
        vertices.append(spl.mesh.Vertex(abs( i[0] ), abs( i[1] ), abs( i[2] ), _id = index))
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

