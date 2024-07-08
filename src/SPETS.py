import blueprint.bphandler as bphandler
import blueprint.filehandler as filehandler
import blueprint.out as out

import mesh.objhandler as objhandler

import typer

app = typer.Typer()

@app.command()
def importer(pathToObj: str, asVehicle: str = ""):
    """
    Import .obj file as sprocket compartment or into vehicle if --asVehicle is specified

    if --asVehicle is specified, then put faction and vehicle in the format "Faction.Vehicle", including quotes
    """
    FACTIONSFOLDER = filehandler.get_factions_folder()
    FACTIONS = filehandler.get_factions(FACTIONSFOLDER)

    print(asVehicle)

    faction = None
    while faction not in FACTIONS:
        faction = input("Faction: ")
        if faction not in FACTIONS:
            print("Faction not found, please choose from " + str(FACTIONS))

if __name__ == "__main__":
    app()