import copy

def get_vuid(data: dict, partName: str) -> int:
    """
    Get vuid given part name
    """
    vuid = None
    for bp in data['blueprints']:
        if bp['blueprint']['name'] == partName:
            vuid = bp['blueprint']['bodyMeshVuid']
    
    return vuid