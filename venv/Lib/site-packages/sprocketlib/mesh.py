import copy

class Vertex:
    def __init__(self, x, y, z, _id = 0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.coords = [x, y, z]
        self.id = _id
    
    def get_coords_as_str(self) -> str:
        return str(self.coords)[1:-1]

class Face:
    def __init__(self, v1: Vertex, v2: Vertex, v3: Vertex, v4: Vertex = None, thickness = 1) -> None:
        if v4 is None:
            self.vertices = [v1, v2, v3]
            self.thickness = [thickness, thickness, thickness]
        else:
            self.vertices = [v1, v2, v3, v4]
            self.thickness = [thickness, thickness, thickness, thickness]
    
    def jsonify(self) -> str:
        v = [i.id for i in copy.deepcopy(self.vertices)]
        t = copy.deepcopy(self.thickness)
        out = {
            'v': v,
            't':t,
        }
        return str(out)

class Face_IDOnly:
    def __init__(self, id1, id2, id3, thickness = 1):
        self.vertex_ids = [id1, id2, id3]
        self.thickness = [thickness, thickness, thickness]
    
    def jsonify(self) -> str:
        v = copy.deepcopy(self.vertex_ids)
        t = copy.deepcopy(self.thickness)
        out = {
            'v': v,
            't':t,
        }
        return out

