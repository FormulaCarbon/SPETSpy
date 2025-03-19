#   Handle parsing of .obj files

def parse_obj(file_path: str) -> tuple:
    vertices = []
    faces = []

    with open(file_path, 'r') as file:
        for line in file:
            tokens = line.split(' ')
            if tokens[0] == 'v':
                vertices.append(list(map(float, tokens[1:])))
            elif tokens[0] == 'f':
                vList = []
                for vSet in tokens[1:]:
                    vTokens = vSet.split('/')
                    vList.append(int(vTokens[0]))
                faces.append(vList)
    
    return (vertices, faces)

def generate_edges(faces: list) -> list:
    edges = []

    for face in faces:
        for i in range(len(face)-1):
            edges.append([face[i], face[i+1]])
        edges.append([face[-1], face[0]])

    return edges

def delete_duplicate_edges(edges: list) -> list:
    cleanedEdges = []
    for edge in edges:
        if edge not in cleanedEdges and [edge[1], edge[0]] not in cleanedEdges:
            cleanedEdges.append(edge)
    
    return cleanedEdges