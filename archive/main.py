from test import out, vuid, vehicle, vehicleFolder
import json, pprint

vData = json.load(open(vehicleFolder + '/' + vehicle, 'r'))

for mesh in vData['meshes']:
    if mesh['vuid'] == vuid:
        mesh['meshData']['mesh'] = out['meshes'][0]['meshData']['mesh']

with open(vehicleFolder + '/' + vehicle, 'w') as vFile:
    json.dump(vData, vFile)
    vFile.close()


print(out['meshes'][0]['meshData']['mesh'])