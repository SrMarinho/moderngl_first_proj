import socket
import dearpygui.dearpygui as dpg
import client
import threading
import json

guiWidth, guiHeight = 200, 300
dpg.create_context()

HOST = "127.0.0.1"
PORT = 12345

client = client.Client(HOST, PORT)
client.send({'function': 'get_scene'})

    
with dpg.window(label="scene", width=guiWidth + 35, height=guiHeight, pos=(0, 0)):
    dpg.add_combo([1, 2, 3, 4], default_value=1)
    dpg.add_text(client.data)

dpg.create_viewport(title='Custom Title', width=guiWidth, height=guiHeight)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()