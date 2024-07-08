import dearpygui.dearpygui as dpg
import backend
import os
import getpass

dpg.create_context()

def callback(sender, app_data, user_data):
    print("Sender: ", sender)
    print("App Data: ", app_data)

def get_vehicles(sender, app_data):
    vehicleFolder = f"C:/Users/{getpass.getuser()}/OneDrive/Documents/My Games/Sprocket/Factions/{app_data}/Blueprints/Vehicles"
    vehicles = [name[:-10] for name in os.listdir(vehicleFolder) if os.path.isfile(os.path.join(vehicleFolder, name)) and os.path.splitext(os.path.join(vehicleFolder, name))[1] == '.blueprint']
    print(app_data)
    dpg.set_value("vehicleslist","##".join(vehicles))
    print(dpg.get_value("vehicleslist").split("##"))


with dpg.value_registry():
    dpg.add_bool_value(default_value=True, tag="bool_value")
    dpg.add_string_value(default_value="", tag="vehicleslist")

with dpg.file_dialog(directory_selector=False, show=False, callback=callback, id="file_dialog_id", width=700 ,height=400):
    dpg.add_file_extension("", color=(150, 255, 150, 255))
    dpg.add_file_extension(".blueprint", color=(0, 255, 255, 255))


with dpg.window(tag="Primary Window"):
    dpg.add_text("Sprocket 3D Model Importer")
    dpg.add_combo(items = tuple(backend.get_factions()), label = 'Faction', callback = get_vehicles)
    dpg.add_combo(items = tuple(dpg.get_value("vehicleslist").split("##")), label = 'Vehicle')
    dpg.add_button(label="File Selector", callback=lambda: dpg.show_item("file_dialog_id"))

dpg.create_viewport(title='SPETSpy', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()