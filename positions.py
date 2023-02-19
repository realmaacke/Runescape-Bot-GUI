class Init:
    Banker_pos_x = 0
    Banker_pos_y = 0

    Grand_exchange_pos_x = 0
    Grand_exchange_pos_y = 0

    def __init__(self, mouse):
        self.mouse = mouse 

    def saveBankerPosition(self, x, y, button, pressed):
        if button == self.mouse.Button.left:  
            if pressed:
                Init.Banker_pos_x = Init.Banker_pos_x + x
                Init.Banker_pos_y = Init.Banker_pos_y + y
                return False
                
        else:
            print("User your left click")

    def start(self):
        print("Drag your cursor to the Banker and left click: ")
        listener = self.mouse.Listener(on_click=self.saveBankerPosition)
        listener.start()
        listener.join()
        