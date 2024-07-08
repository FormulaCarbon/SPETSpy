import json, pprint, sys

from sprocketlib.parts import *

def parse_blueprint(filename, rawText = False):
    if rawText:
        return json.loads(filename)
    with open(filename, 'r') as f:
        data = json.load(f)
    f.close()
    return data

# TODO: add meshes and objects into BluePrint class

class BluePrint:
    def __init__(self, path:str) -> None:
        self.path = path
        self.data = parse_blueprint(self.path)
        self.blueprints = []

    def __str__(self) -> str:
        return pprint.pformat(self.data)
    
    def _str_to_class(self, str):
        return getattr(sys.modules[__name__], str)

    def get_header(self):
        return self.data['header']
    
    def get_part_id(self, name:str, type:str):
        for blueprint in self.data['blueprints']:
            if type == blueprint['type']:
                info = blueprint['blueprint']
                if name == info['name']:
                    return blueprint['id']
    
    def get_blueprints(self):
        return self.data['blueprints']
    
    def load_blueprints(self):
        bps = self.data['blueprints']
        out = []
        for i in bps:
            t = i['type'][0].upper() + i['type'][1:]
            match t:
                case 'PaintJobRegister':
                    out.append(PaintJobRegister(i['id']))
                case 'PaintJob':
                        out.append(PaintJob(i['id']))
                case 'PaintJob':
                        out.append(PaintJob(i['id']))
                case 'Chassis':
                        out.append(Chassis(i['id']))
                case 'Structure':
                        out.append(Structure(i['id']))
                case 'VerticalSplitHull':
                        out.append(VerticalSplitHull(i['id']))
                case 'Engine':
                        out.append(Engine(i['id']))
                case 'Transmission':
                        out.append(Transmission(i['id']))
                case 'Track':
                        out.append(Track(i['id']))
                case 'TrackWheelMount':
                        out.append(TrackWheelMount(i['id']))
                case 'TrackWheel':
                        out.append(TrackWheel(i['id']))
                case 'TrackWheelMount':
                        out.append(TrackWheelMount(i['id']))
                case 'TrackWheel':
                        out.append(TrackWheel(i['id']))
                case 'TrackWheelArray':
                        out.append(TrackWheelArray(i['id']))
                case 'TrackWheelMount':
                        out.append(TrackWheelMount(i['id']))
                case 'TrackWheel':
                        out.append(TrackWheel(i['id']))
                case 'TrackWheelArray':
                        out.append(TrackWheelArray(i['id']))
                case 'TrackWheelMount':
                        out.append(TrackWheelMount(i['id']))
                case 'TrackWheel':
                        out.append(TrackWheel(i['id']))
                case 'TrackBelt':
                        out.append(TrackBelt(i['id']))
                case 'Suspension':
                        out.append(Suspension(i['id']))
                case 'TorsionBar':
                        out.append(TorsionBar(i['id']))
                case 'TurretRing':
                        out.append(TurretRing(i['id']))
                case 'Turret':
                        out.append(Turret(i['id']))
                case 'Motor':
                        out.append(Motor(i['id']))
                case 'TurretBasket':
                        out.append(TurretBasket(i['id']))
                case 'Structure':
                        out.append(Structure(i['id']))
                case 'LayingDrive':
                        out.append(LayingDrive(i['id']))
                case 'ShellSlot':
                        out.append(ShellSlot(i['id']))
                case 'Cannon':
                        out.append(Cannon(i['id']))
                case 'CannonInstance':
                        out.append(CannonInstance(i['id']))
                case 'AmmoRack':
                        out.append(AmmoRack(i['id']))
                case 'CrewSeat':
                        out.append(CrewSeat(i['id']))
                case 'Posture':
                        out.append(Posture(i['id']))
                case 'CrewSeat':
                        out.append(CrewSeat(i['id']))
                case 'Posture':
                        out.append(Posture(i['id']))
                case 'CrewSeat':
                        out.append(CrewSeat(i['id']))
                case 'Posture':
                        out.append(Posture(i['id']))
                case 'CrewSeat':
                        out.append(CrewSeat(i['id']))
                case 'Posture':
                        out.append(Posture(i['id']))
                case 'CrewSeat':
                        out.append(CrewSeat(i['id']))
                case 'Posture':
                        out.append(Posture(i['id']))
                case 'FuelTank':
                        out.append(FuelTank(i['id']))
                case 'FuelTank':
                        out.append(FuelTank(i['id']))
                case 'FuelTank':
                        out.append(FuelTank(i['id']))
                case 'FuelTank':
                        out.append(FuelTank(i['id']))
                case 'DecalTransform':
                        out.append(DecalTransform(i['id']))
                case 'Decal':
                        out.append(Decal(i['id']))
                case 'DecalTransform':
                        out.append(DecalTransform(i['id']))
                case 'Decal':
                        out.append(Decal(i['id']))
                case 'DecalTransform':
                        out.append(DecalTransform(i['id']))
                case 'Decal':
                        out.append(Decal(i['id']))
                case 'ShellSlot':
                        out.append(ShellSlot(i['id']))
                case 'AmmoRack':
                        out.append(AmmoRack(i['id']))
                case 'DecalTransform':
                        out.append(DecalTransform(i['id']))
                case 'Decal':
                        out.append(Decal(i['id']))
                case 'Structure':
                        out.append(Structure(i['id']))
                case 'Structure':
                        out.append(Structure(i['id']))
                case 'Structure':
                        out.append(Structure(i['id']))
                case 'DecalTransform':
                        out.append(DecalTransform(i['id']))
                case 'Decal':
                        out.append(Decal(i['id']))
                case 'DecalTransform':
                        out.append(DecalTransform(i['id']))
                case 'Decal':
                        out.append(Decal(i['id']))
                case 'DecalTransform':
                        out.append(DecalTransform(i['id']))
                case 'Decal':
                        out.append(Decal(i['id']))
                case 'DecalTransform':
                        out.append(DecalTransform(i['id']))
                case 'Decal':
                        out.append(Decal(i['id']))
        self.blueprints = out
        return out
    
    def load_blueprints_properties(self):
        for i in self.blueprints:
            i.load(self.data)

        return self.blueprints