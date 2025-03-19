import src.objHandler as objHandler
import src.bpHandler as bpHandler

v, f = objHandler.parse_obj("")
e = objHandler.generate_edges(f)

f = bpHandler.generate_face_info(f)
e = objHandler.delete_duplicate_edges(e)
ef = bpHandler.generate_empty_edge_flags(len(e))

v = bpHandler.combine_all(v)
e = bpHandler.combine_all(e)

bp = bpHandler.fill_compartment_template("test", v, e, ef, f)
print(bp)
