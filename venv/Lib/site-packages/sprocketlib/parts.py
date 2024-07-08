import pprint

class Base:
    def __init__(self, id):
        self.type = 'base'
        self.id = id
        self.data = None

    def __str__(self) -> str:
        return pprint.pformat(self.data)
    
class PaintJobRegister(Base):
    def __init__(self, id):
        self.id = id
        self.type = "paintJobRegister"
        self.name = None
        self.description = None
        self.paintJobIDs = None
        self.data = None
    
    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint
        
        self.name = info['name']
        self.description = info['description']
        self.paintJobIDs = info['paintJobIDs']

class PaintJob(Base):
    def __init__(self, id):
        self.id = id
        self.type = "paintJob"
        self.name = None
        self.description = None
        self.colourMapUrl = None
        self.scale = None
        self.roughness = None
        self.r = None
        self.g = None
        self.b = None
        self.saturation = None
        self.condition = None
        self.grime = None
    
    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint
        
        self.name = info['name']
        self.description = info['description']
        self.colourMapUrl = info['colourMapUrl']
        self.scale = info['scale']
        self.roughness = info['roughness']
        self.r = info['r']
        self.g = info['g']
        self.b = info['b']
        self.saturation = info['saturation']
        self.condition = info['condition']
        self.grime = info['grime']

class Chassis(Base):
    def __init__(self, id):
        self.id = id
        self.type = "chassis"
        self.name = None
        self.description = None
        self.length = None
        self.width = None
        self.groundClearance = None
    
    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint
        
        self.name = info['name']
        self.description = info['description']
        self.length = info['length']
        self.width = info['width']
        self.groundClearance = info['groundClearance']

class Structure(Base):
    def __init__(self, id):
        self.id = id
        self.type = "structure"
        self.name = None
        self.description = None
        self.armourVolume = None
        self.bodyMeshVuid = None
        self.partRepositioning = None
    
    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint
        
        self.name = info['name']
        self.description = info['description']
        self.armourVolume = info['armourVolume']
        self.bodyMeshVuid = info['bodyMeshVuid']
        self.partRepositioning = info['partRepositioning']

class VerticalSplitHull(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'verticalSplitHull'
        self.name = None
        self.description = None
        self.generationData = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.generationData = info['generationData']
        
class Engine(Base):
    def __init__(self, id):
        self.id = id
        self.type = "engine"
        self.name = None
        self.description = None
        self.cylinders = None
        self.idleRPM = None
        self.cylinderDisplacement = None
        self.tech = None
        self.targetMinRPM = None
        self.targetMaxRPM = None
        self.torqueCoeff = None
        self.revLimit = None
    
    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint
        
        self.name = info['name']
        self.description = info['description']
        self.cylinders = info['cylinders']
        self.idleRPM = info['idleRPM']
        self.cylinderDisplacement = info['cylinderDisplacement']
        self.tech = info['tech']
        self.targetMinRPM = info['targetMinRPM']
        self.targetMaxRPM = info['targetMaxRPM']
        self.torqueCoeff = info['torqueCoeff']
        self.revLimit = info['revLimit']

class Transmission(Base):
    def __init__(self, id):
        self.id = id
        self.type = "transmission"
        self.name = None
        self.description = None
        self.autoInputTorque = None
        self.maxInputTorque = None
        self.autoResistanceTorque = None
        self.maxResistanceTorque = None
        self.d = None
        self.r = None
    
    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint
        
        self.name = info['name']
        self.description = info['description']
        self.autoInputTorque = info['autoInputTorque']
        self.maxInputTorque = info['maxInputTorque']
        self.autoResistanceTorque = info['autoResistanceTorque']
        self.maxResistanceTorque = info['maxResistanceTorque']
        self.d = info['d']
        self.r = info['r']

class Track(Base):
    def __init__(self, id):
        self.id = id
        self.type = "track"
        self.name = None
        self.description = None
        self.separation = None
        self.length = None
        self.rrCoeff = None
        self.brake = None
        self.autoBrake = None
        self.rollersEnabled = None
        self.matchChassis = None
        self.frontalTransmission = None
    
    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint
        
        self.name = info['name']
        self.description = info['description']
        self.separation = info['separation']
        self.length = info['length']
        self.rrCoeff = info['rrCoeff']
        self.brake = info['brake']
        self.autoBrake = info['autoBrake']
        self.rollersEnabled = info['rollersEnabled']
        self.matchChassis = info['matchChassis']
        self.frontalTransmission = info['frontalTransmission']

class TrackWheelMount(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'trackWheelMount'
        self.name = None
        self.description = None
        self.mountID = None
        self.scale = None
        self.x = None
        self.y = None
        self.z = None
        self.rearFacing = None
    
    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint
        
        self.name = info['name']
        self.description = info['description']
        self.mountID = info['mountID']
        self.scale = info['scale']
        self.x = info['x']
        self.y = info['y']
        self.z = info['z']
        self.rearFacing = info['rearFacing']

class TrackWheel(Base):
    def __init__(self, id):
        self.id = id
        self.type = "trackWheel"
        self.name = None
        self.description = None
        self.wheelID = None
        self.perAxle = None
        self.spacingOnAxle = None
        self.xOffset = None
        self.diameter = None
        self.width = None
    
    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint
        
        self.name = info['name']
        self.description = info['description']
        self.wheelID = info['description']
        self.perAxle = info['perAxle']
        self.spacingOnAxle = info['spacingOnAxle']
        self.xOffset = info['xOffset']
        self.diameter = info['diameter']
        self.width = info['width']

class TrackWheelArray(Base):
    def __init__(self, id):
        self.id = id
        self.type = "trackWheelArray"
        self.spacing = None
        self.length = None
        self.interleaveOverlapFraction = None
        self.groupSpacing = None
        self.perGroup = None
        self.groupingOffset = None
        self.zOrigen = None
        self.yOrigin = None
        self.xOrigin = None
        self.zOffset = None
        self.yOffset = None
        self.xOffset = None
        self.syncLengthEnabled = None
        self.angle = None
        self.lockAngle = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint
        
        self.name = info['name']
        self.description = info['description']
        self.spacing = info['spacing']
        self.length = info['length']
        self.interleaveOverlapFraction = info['interleaveOverlapFraction']
        self.groupSpacing = info['groupSpacing']
        self.perGroup = info['perGroup']
        self.groupingOffset = info['groupingOffset']
        self.zOrigen = info['zOrigin']
        self.yOrigin = info['yOrigin']
        self.xOrigin = info['xOrigin']
        self.zOffset = info['zOffset']
        self.yOffset = info['yOffset']
        self.xOffset = info['xOffset']
        self.syncLengthEnabled = info['syncLengthEnabled']
        self.angle = info['angle']
        self.lockAngle = info['lockAngle']

class TrackBelt(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'trackBelt'
        self.name = None
        self.description = None
        self.segmentID = None
        self.x = None
        self.y = None
        self.z = None
        self.pitch = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.segmentID = info['segmentID']
        self.x = info['x']
        self.y = info['y']
        self.z = info['z']
        self.pitch = info['pitch']

class Suspension(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'suspension'
        self.name = None
        self.description = None
        self.suspensionID = None
        self.targetAngle = None
        self.upTravelLimit = None
        self.damper = None
        self.armLength = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.suspensionID = info['suspensionID']
        self.targetAngle = info['targetAngle']
        self.upTravelLimit = info['upTravelLimit']
        self.damper = info['damper']
        self.armLength = info['armLength']

class TorsionBar(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'torsionBar'
        self.name = None
        self.description = None
        self.torsionBarLength = None
        self.torsionBarDiameter = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.torsionBarLength = info['torsionBarLength']
        self.torsionBarDiameter = info['torsionBarDiameter']

class TurretRing(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'turretRing'
        self.name = None
        self.description = None
        self.ringHeight = None
        self.ringDiameter = None
        self.ringThickness = None
        self.motorVuid = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.ringHeight = info['ringHeight']
        self.ringDiameter = info['ringDiameter']
        self.ringThickness = info['ringThickness']
        self.motorVuid = info['motorVuid']

class Turret(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'turret'
        self.name = None
        self.description = None
        self.maxRot = None
        self.minRot = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.maxRot = info['maxRot']
        self.minRot = info['minRot']

class Motor(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'motor'
        self.name = None
        self.description = None
        self.torque = None
        self.ratio = None
        self.type = None
        self.resist = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.torque = info['torque']
        self.ratio = info['ratio']
        self.type = info['type']
        self.resist = info['resist']

class TurretBasket(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'turretBasket'
        self.name = None
        self.description = None
        self.segments = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.segments = info['segments']

class Structure(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'structure'
        self.name = None
        self.description = None
        self.armourVolume = None
        self.bodyMeshVuid = None
        self.partRepositioning = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.armourVolume = info['armourVolume']
        self.bodyMeshVuid = info['bodyMeshVuid']
        self.partRepositioning = info['partRepositioning']

class LayingDrive(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'layingDrive'
        self.name = None
        self.description = None
        self.elevation = None
        self.azimuth = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.elevation = info['elevation']
        self.azimuth = info['azimuth']

class ShellSlot(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'shellSlot'
        self.name = None
        self.description = None
        self.diameter = None
        self.propellantLength = None
        self.generatedProjectiles = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.diameter = info['diameter']
        self.propellantLength = info['propellantLength']
        self.generatedProjectiles = info['generatedProjectiles']

class Cannon(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'cannon'
        self.name = None
        self.description = None
        self.caliber = None
        self.breechLength = None
        self.muzzle = None
        self.segments = None
        self.counterweight = None
        self.muzzleMass = None
        self.K = None
        self.PSI = None
        self.shellID = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.caliber = info['caliber']
        self.breechLength = info['breechLength']
        self.muzzle = info['muzzle']
        self.segments = info['segments']
        self.counterweight = info['counterweight']
        self.muzzleMass = info['muzzleMass']
        self.K = info['K']
        self.PSI = info['PSI']
        self.shellID = info['shellID']

class CannonInstance(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'cannonInstance'
        self.name = None
        self.description = None
        self.flags = None
        self.fireGroup = None
        self.fireDelay = None
        self.sightVuid = None
        self.barrelVuids = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.flags = info['flags']
        self.fireGroup = info['fireGroup']
        self.fireDelay = info['fireDelay']
        self.sightVuid = info['sightVuid']
        self.barrelVuids = info['barrelVuids']

class AmmoRack(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'ammoRack'
        self.name = None
        self.description = None
        self.diameter = None
        self.length = None
        self.x = None
        self.y = None
        self.z = None
        self.shellTypeGuid = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.diameter = info['diameter']
        self.length = info['length']
        self.x = info['x']
        self.y = info['y']
        self.z = info['z']
        self.shellTypeGuid = info['shellTypeGuid']

class CrewSeat(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'crewSeat'
        self.name = None
        self.description = None
        self.operatedBehaviours = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.operatedBehaviours = info['operatedBehaviours']

class Posture(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'posture'
        self.name = None
        self.description = None
        self.angle = None
        self.height = None
        self.feetForward = None
        self.leftArmUpAngle = None
        self.rightArmUpAngle = None
        self.leftArmInAngle = None
        self.rightArmInAngle = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.angle = info['angle']
        self.height = info['height']
        self.feetForward = info['feetForward']
        self.leftArmUpAngle = info['leftArmUpAngle']
        self.rightArmUpAngle = info['rightArmUpAngle']
        self.leftArmInAngle = info['leftArmInAngle']
        self.rightArmInAngle = info['rightArmInAngle']

class FuelTank(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'fuelTank'
        self.name = None
        self.description = None
        self.x = None
        self.y = None
        self.z = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.x = info['x']
        self.y = info['y']
        self.z = info['z']

class DecalTransform(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'decalTransform'
        self.name = None
        self.description = None
        self.x = None
        self.y = None
        self.z = None
        self.flags = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.name = info['name']
        self.description = info['description']
        self.x = info['x']
        self.y = info['y']
        self.z = info['z']
        self.flags = info['flags']

class Decal(Base):
    def __init__(self, id):
        self.id = id
        self.type = 'decal'
        self.referenceLocator = None
        self.name = None
        self.description = None
        self.fakeUser = None
        self.ID = None
        self.userCount = None

    def load(self, data):
        for blueprint in data['blueprints']:
            if self.id == blueprint['id']:
                info = blueprint['blueprint']
                self.data = blueprint

        self.referenceLocator = info['ReferenceLocator']
        self.name = info['Name']
        self.description = info['Description']
        self.fakeUser = info['FakeUser']
        self.ID = info['ID']
        self.userCount = info['UserCount']