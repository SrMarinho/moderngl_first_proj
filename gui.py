import dearpygui.dearpygui as dpg
import client

def obj_selected(sender, data, user_data):
    
    dpg.set_item_user_data(positionX, {'obj_name': data, 'pos': 0})
    dpg.set_item_user_data(positionY, {'obj_name': data, 'pos': 1})
    dpg.set_item_user_data(positionZ, {'obj_name': data, 'pos': 2})
    
    dpg.set_item_user_data(rotationX, {'obj_name': data, 'rot': 0})
    dpg.set_item_user_data(rotationY, {'obj_name': data, 'rot': 1})
    dpg.set_item_user_data(rotationZ, {'obj_name': data, 'rot': 2})
    
    dpg.set_item_user_data(scaleX, {'obj_name': data, 'scale': 0})
    dpg.set_item_user_data(scaleY, {'obj_name': data, 'scale': 1})
    dpg.set_item_user_data(scaleZ, {'obj_name': data, 'scale': 2})
    
    #set slider value to position in scene
    dpg.set_value(positionX, scene['scene'][data]['pos'][0])
    dpg.set_value(positionY, scene['scene'][data]['pos'][1])
    dpg.set_value(positionZ, scene['scene'][data]['pos'][2])
    
    #set slider value to rotation in scene
    dpg.set_value(rotationX, scene['scene'][data]['rot'][0])
    dpg.set_value(rotationY, scene['scene'][data]['rot'][1])
    dpg.set_value(rotationZ, scene['scene'][data]['rot'][2])
    
    #set slider value to rotation in scene
    dpg.set_value(scaleX, scene['scene'][data]['scale'][0])
    dpg.set_value(scaleY, scene['scene'][data]['scale'][1])
    dpg.set_value(scaleZ, scene['scene'][data]['scale'][2])
    
    
    # user_data['client'].send({"function": {user_data['function'] : {"params": {"obj" : data}}}})
    
def set_obj_pos(sender, data, user_data):
    sclient.send('set_obj_pos', {'obj_name': user_data['obj_name'], list(user_data)[1]: {user_data[list(user_data)[1]]: data}})
        

HOST = "127.0.0.1"
PORT = 12345

sclient = client.Client(HOST, PORT)

dpg.create_context()

win_settings = sclient.send('get_win_setting')

guiWidth, guiHeight = 200, 400

scene = sclient.send('get_scene')

with dpg.window(label="scene", width=guiWidth + 35, height=guiHeight, pos=(0, 0)):
    obj_selected_index = dpg.add_listbox(
        items=list(scene['scene']),
        default_value=list(scene['scene'])[0] if len(scene['scene']) > 0 else '',
        callback=obj_selected,
    )
    #position
    dpg.add_text(
        label="position:",
        default_value="position:"
    )
    positionX = dpg.add_slider_float(
        label="x",
        default_value=scene['scene'][dpg.get_value(obj_selected_index)]['pos'][0] if len(scene['scene']) > 0 else 0,
        min_value=-5,
        max_value=5,
        callback=set_obj_pos,
        user_data={'obj_name': dpg.get_value(obj_selected_index), 'pos': 0}
    )
    positionY = dpg.add_slider_float(
        label="y",
        default_value=scene['scene'][dpg.get_value(obj_selected_index)]['pos'][1] if len(scene['scene']) > 0 else 0,
        min_value=-5,
        max_value=5,
        callback=set_obj_pos,
        user_data={'obj_name': dpg.get_value(obj_selected_index), 'pos': 1}
    )
    
    positionZ = dpg.add_slider_float(
        label="z",
        default_value=scene['scene'][dpg.get_value(obj_selected_index)]['pos'][2] if len(scene['scene']) > 0 else 0,
        min_value=-10,
        max_value=0,
        callback=set_obj_pos,
        user_data={'obj_name': dpg.get_value(obj_selected_index), 'pos': 2}
    )
    #rotation
    dpg.add_text(
        label="rotation:",
        default_value="rotation:"
    )
    rotationX = dpg.add_slider_float(
        label="x",
        default_value=scene['scene'][dpg.get_value(obj_selected_index)]['rot'][0] if len(scene['scene']) > 0 else 0,
        min_value=0,
        max_value=360,
        callback=set_obj_pos,
        user_data={'obj_name': dpg.get_value(obj_selected_index), 'rot': 0}
    )
    rotationY = dpg.add_slider_float(
        label="y",
        default_value=scene['scene'][dpg.get_value(obj_selected_index)]['rot'][1] if len(scene['scene']) > 0 else 0,
        min_value=0,
        max_value=360,
        callback=set_obj_pos,
        user_data={'obj_name': dpg.get_value(obj_selected_index), 'rot': 1}
    )
    rotationZ = dpg.add_slider_float(
        label="z",
        default_value=scene['scene'][dpg.get_value(obj_selected_index)]['rot'][2] if len(scene['scene']) > 0 else 0,
        min_value=0,
        max_value=360,
        callback=set_obj_pos,
        user_data={'obj_name': dpg.get_value(obj_selected_index), 'rot': 2}
    )
    #scale
    dpg.add_text(
        label="scale:",
        default_value="scale:"
    )
    scaleX = dpg.add_slider_float(
        label="x",
        default_value=scene['scene'][dpg.get_value(obj_selected_index)]['scale'][0] if len(scene['scene']) > 0 else 0,
        min_value=0,
        max_value=10,
        callback=set_obj_pos,
        user_data={'obj_name': dpg.get_value(obj_selected_index), 'scale': 0}
    )
    scaleY = dpg.add_slider_float(
        label="y",
        default_value=scene['scene'][dpg.get_value(obj_selected_index)]['scale'][1] if len(scene['scene']) > 0 else 0,
        min_value=0,
        max_value=10,
        callback=set_obj_pos,
        user_data={'obj_name': dpg.get_value(obj_selected_index), 'scale': 1}
    )
    scaleZ = dpg.add_slider_float(
        label="z",
        default_value=scene['scene'][dpg.get_value(obj_selected_index)]['scale'][2] if len(scene['scene']) > 0 else 0,
        min_value=0,
        max_value=10,
        callback=set_obj_pos,
        user_data={'obj_name': dpg.get_value(obj_selected_index), 'scale': 2}
    )

dpg.create_viewport(title='Custom Title', width=guiWidth, height=guiHeight, x_pos=win_settings['position'][0] + win_settings['size'][0], y_pos=win_settings['position'][1] - 35)
dpg.setup_dearpygui()

dpg.show_viewport()
# dpg.start_dearpygui()
while dpg.is_dearpygui_running():
    # print(dpg.get_value(obj_selected_index))
    

    
    #update position in scene
    scene['scene'][dpg.get_value(obj_selected_index)]['pos'][0] = dpg.get_value(positionX)
    scene['scene'][dpg.get_value(obj_selected_index)]['pos'][1] = dpg.get_value(positionY)
    scene['scene'][dpg.get_value(obj_selected_index)]['pos'][2] = dpg.get_value(positionZ)
    #update rotation in scene
    scene['scene'][dpg.get_value(obj_selected_index)]['rot'][0] = dpg.get_value(rotationX)
    scene['scene'][dpg.get_value(obj_selected_index)]['rot'][1] = dpg.get_value(rotationY)
    scene['scene'][dpg.get_value(obj_selected_index)]['rot'][2] = dpg.get_value(rotationZ)
    #update scale in scene
    scene['scene'][dpg.get_value(obj_selected_index)]['scale'][0] = dpg.get_value(rotationX)
    scene['scene'][dpg.get_value(obj_selected_index)]['scale'][1] = dpg.get_value(rotationY)
    scene['scene'][dpg.get_value(obj_selected_index)]['scale'][2] = dpg.get_value(rotationZ)
    dpg.render_dearpygui_frame()
    
dpg.set_exit_callback(sclient.send('exit'))