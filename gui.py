import socket
import dearpygui.dearpygui as dpg
import client
import threading
import json

dpg.create_context()

def obj_selected(sender, data, user_data):
    user_data['client'].send({"function": {user_data['function'] : {"obj" : data}}})
    
def set_pos(sender, data, user_data):
    user_data['client'].send({"function": {user_data['function'] : {"x" : data}}})

guiWidth, guiHeight = 200, 300

HOST = "127.0.0.1"
PORT = 12345

client = client.Client(HOST, PORT)
client.send({'function': 'get_scene'})
scene = None
while scene == None:
    scene = client.data
print(scene['scene'][0])

with dpg.window(label="scene", width=guiWidth + 35, height=guiHeight, pos=(0, 0)):
    dpg.add_text(scene['scene'][0]['vao_name'])
    dpg.add_combo(items=[1, 2, 3, 4], default_value=1, callback=obj_selected, user_data={'client': client, 'function': 'set_pos'})
    dpg.add_slider_float(label="x", default_value=scene['scene'][0]['pos'][0], min_value=0, max_value=-10)
    dpg.add_slider_float(label="y", default_value=scene['scene'][0]['pos'][1], min_value=0, max_value=-10)
    dpg.add_slider_float(label="z", default_value=scene['scene'][0]['pos'][2], min_value=0, max_value=-10)

dpg.create_viewport(title='Custom Title', width=guiWidth, height=guiHeight)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()