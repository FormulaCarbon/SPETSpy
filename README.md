# SPETSpy
SProcket Editing ToolS (python version). Original C++ version made by Argore

## Usage

### Recommended: Run .exe
On the github page, go to releases and download the latest `SPETSpy_version.exe`. Double click to run, answer the questions, and let the program do the rest.
If you get the error `Factions folder not found at defualt location, please input here:`, give it the FULL path to the Sprockt\Factions folder. For example, mine is `C:/Users/siddh/OneDrive/Documents/My Games/Sprocket/Factions`. When entering the path to the .obj file, make sure there is no quotation marks around the path, whcih Windows may insert if you do `Copy path as text`.

### Run as command line command (python version only):
Clone this repository and navigate to src folder. Run this command:
`py -m main`

## Todo
 - Implement exporting
 - Implement face coloring

## Building
In order to modify and build the program, create a python virtual environment named `venv` by doing `py -m venv venv`. Install pyinstaller, which is needed to build, by running `pip install pyinstaller`. Then run `build.ps1` or `pyinstaller src/main.py --onefile --name SPETSpy1_2`.