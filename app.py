#GUI
import dearpygui.dearpygui as dpg
# Functionality
from pynput import mouse

#classes
from positions import Init
from notifications import Notify
from Controller import Controlls
from actions import Actions

dpg.create_context()
dpg.create_viewport(title="Runescape-Bot", width=400, height=400)


def BankerPosCallback():
    instance.start()
    pos = "X: " + str(instance.Banker_pos_x) + " | Y: " + str(instance.Banker_pos_y)
    dpg.set_value("banker_pos", pos)

def StartCallBack():
    print("Start Callback")
    name = dpg.get_value("item")
    ItemCount = dpg.get_value("count")
    xTimes = dpg.get_value("times")
    duration = dpg.get_value("duration")
    controll.notifications = dpg.get_value('notifications')

    actions.Start(instance.Banker_pos_x, instance.Banker_pos_y, name, ItemCount, duration, xTimes)

def RestartCallBack():
    actions.restart = True
    dpg.set_value("running", "Not Running")
    dpg.set_value("item", "Item")
    dpg.set_value("count", 0)
    dpg.set_value("times", 0)
    dpg.set_value("duration", 0)


with dpg.window(label="Bot-Config", width=400, height=400):
    dpg.add_input_text(label="Item Name", default_value="Item", tag="item")
    dpg.add_input_int(label="Item count", tag="count")
    dpg.add_input_int(label="Ammount X time", tag="times")
    dpg.add_input_int(label="duration", tag="duration")

    dpg.add_button(label="Select Banker position", callback=BankerPosCallback)
    dpg.add_same_line()
    dpg.add_text(label="X: | Y: ", tag="banker_pos")

    dpg.add_checkbox(label="Notify", tag="notifications")

    dpg.add_button(label="start", callback=StartCallBack)
    dpg.add_same_line()
    dpg.add_button(label="restart", callback=RestartCallBack)
    dpg.add_same_line()
    dpg.add_text(label="Not Running", color=[52, 235, 103], tag="running")

    dpg.add_text(label="0 / 0", tag="rotation")


dpg.setup_dearpygui()
dpg.show_viewport()


while dpg.is_dearpygui_running():
    instance = Init(mouse)
    notify = Notify()
    controll = Controlls()
    actions = Actions()

    rotation = str(actions.times) + " / " + str(actions.Rotations)
    dpg.set_value('rotation',rotation)

    if actions.times >= actions.Rotations:
        actions.Complete = True
    if actions.times >= 1 < actions.Rotations:
        dpg.set_value("running", "Running")

    if actions.Complete == True:
        if controll.notifications == True:
            notify.SendNotification(False)
        dpg.set_value("running", "Not Running")

    dpg.render_dearpygui_frame()


dpg.destroy_context()


## comment