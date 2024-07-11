import sprocketlib as spl
import getpass
import os
import json

def load_bp(filepath: str):
    """
    Convert .blueprint file into sprocketlib.base.BluePrint object
    """
    bp = spl.base.BluePrint(filepath)
    
    return bp

def load_bp_as_dict(filepath: str) -> dict:
    """
    Convert .blueprint to python dictionary
    """
    return json.load(open(filepath, 'r'))

def get_factions_folder() -> str:
    """
    Return path to folder containing factions
    """
    return f"C:/Users/{getpass.getuser()}/OneDrive/Documents/My Games/Sprocket/Factions"

def get_factions(factionsFolder: str) -> list:
    """
    Return list of factions
    """
    return [name for name in os.listdir(factionsFolder) if os.path.isdir(os.path.join(factionsFolder, name))]

def get_vehicles_folder(factionsFolder, faction) -> str:
    """
    Return path to folder containing vehicles of a given faction
    """
    return factionsFolder + f'/{faction}/Blueprints/Vehicles'

def get_vehicles(vehiclesFolder: str) -> list:
    """
    Return list of vehicles in a faction
    """
    return [name[:-10] for name in os.listdir(vehiclesFolder) if os.path.isfile(os.path.join(vehiclesFolder, name)) and os.path.splitext(os.path.join(vehiclesFolder, name))[1] == '.blueprint']

