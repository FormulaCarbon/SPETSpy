import json, copy

def combine_all(arr: list) -> list:
    out = []

    for items in arr:
        for item in items:
            out.append(item)

    return out

def generate_face_info(faces: list, thickness = 5) -> dict:
    faceDicts = []
    dictTemplate = {
        "v" : None,
        "t" : None,
        "tm": 16843009,
        "te": 0
    }

    for face in faces:
        temp = copy.deepcopy(dictTemplate)
        temp["v"] = face
        temp["t"] = [thickness for i in range(len(face))]
        if len(face) == 3:
            temp["tm"] = 65793
        #temp["te"] = calculate_te(face)
        faceDicts.append(temp)
        
    print(faceDicts)
    
    return faceDicts

def calculate_te(faces: list) -> int:
    if len(faces) == 4:
        return (faces[0] & 0xFFFF) | ((faces[1] & 0xFFFF) << 16) | ((faces[2] & 0xFFFF) << 32) | ((faces[3] & 0xFFFF) << 48)
    elif len(faces) == 3:
        return (faces[0] & 0xFFFF) | ((faces[1] & 0xFFFF) << 16) | ((faces[2] & 0xFFFF) << 32)
        

def generate_empty_edge_flags(length: int) ->list:
    return [0 for i in range(length)]

def fill_compartment_template(name: str, vertices: list, edges: list, edgeFlags: list, faces: list) -> str:
    filledTemplate = """{
  "v": "0.2",
  "name": "{name}",
  "smoothAngle": 0,
  "gridSize": 1,
  "format": "freeform",
  "mesh": {
    "majorVersion": 0,
    "minorVersion": 3,
    "vertices": {vertices},
    "edges": {edges},
    "edgeFlags": {edgeFlags},
    "faces": {faces}
  },
  "rivets": {
    "profiles": [
      {
        "model": 0,
        "spacing": 0.1,
        "diameter": 0.05,
        "height": 0.025,
        "padding": 0.04
      }
    ],
    "nodes": []
  }
}""".replace("{name}", name).replace("{vertices}", str(vertices)).replace("{edges}", str(edges)).replace("{edgeFlags}", str(edgeFlags)).replace("{faces}", str(faces))
    return filledTemplate