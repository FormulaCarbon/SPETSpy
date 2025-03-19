import objHandler as objHandler
import bpHandler as bpHandler

v, f = objHandler.parse_obj(input("Path to .obj file: "))
e = objHandler.generate_edges(f)

f = bpHandler.generate_face_info(f)
e = objHandler.delete_duplicate_edges(e)
ef = bpHandler.generate_empty_edge_flags(len(e))

v = bpHandler.combine_all(v)
e = bpHandler.combine_all(e)

bp = bpHandler.fill_compartment_template("test", v, e, ef, f)

with open("test.blueprint", 'w') as file:
    file.write(bp)
    file.close()
print(bp)
