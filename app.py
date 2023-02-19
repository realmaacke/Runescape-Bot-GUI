import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Runescape-Bot", width=400, height=400)

with dpg.window(label="Bot-Config", width=400, height=400):
    ItemName = dpg.add_input_text(label="Item Name", default_value="Item")
    ItemCount = dpg.add_input_int(label="Item count")
    InventorySize = dpg.add_input_int(label="How many each time")

    BankerPosButton = dpg.add_button(label="Select Banker position")

    StartButton = dpg.add_button(label="start")



dpg.setup_dearpygui()
dpg.show_viewport()


while dpg.is_dearpygui_running():
    #loop here
    dpg.render_dearpygui_frame()


dpg.destroy_context()