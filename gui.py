import socket
import dearpygui.dearpygui as dpg

def server_client():
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 12345  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

    print(f"Received {data!r}")

server_client()
guiWidth, guiHeight = 200, 300
dpg.create_context()
    
with dpg.window(width=guiWidth + 35, height=guiHeight, pos=(0, 0)):
    dpg.add_combo([1, 2, 3, 4], default_value=1)

dpg.create_viewport(title='Custom Title', width=guiWidth, height=guiHeight)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()