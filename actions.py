import time
import pyautogui as mouse
from random import randrange
from pynput.keyboard import Key, Controller
import math

class Actions:
    Item = ""
    ItemCount = 0
    InventorySize = 0

    Rotations = 0
    times = 0
    Duration = 0

    Complete = False
    restart = False

    banker_position_x = 0
    banker_position_y = 0

    def __init__(self):
        Keyboard = Controller()
        self.keyboard = Keyboard
    
    def Start(self, banker_position_x, banker_position_y, item, count, duration, eachTime):
        Actions.banker_position_x = banker_position_x
        Actions.banker_position_y = banker_position_y

        Actions.Item = item
        Actions.ItemCount = count
        Actions.Duration = duration
        Actions.InventorySize = eachTime

        self.CalculateRotation()
        print("")
        print("This process will take " + str(Actions.Rotations) + "x Times")

        self.InitAction()


    def CalculateRotation(self):
        RotationCount = Actions.ItemCount / Actions.InventorySize
        Actions.Rotations = math.ceil(RotationCount)


    def OnAction(self):
        while Actions.restart == False:
            time.sleep(2)
            mouse.moveTo(Actions.banker_position_x, Actions.banker_position_y)
            mouse.click()
            time.sleep(2)
            self.keyboard.press(Key.f3)
            self.keyboard.release(Key.f3)
            time.sleep(2)
            self.keyboard.press(Key.f3)
            self.keyboard.release(Key.f3)
            time.sleep(3)
            self.keyboard.press(Key.space)
            self.keyboard.release(Key.space)
            time.sleep(Actions.Duration) 
        else:
            return

    def InitAction(self):
        Actions.times = 0
        for _ in range(Actions.Rotations):
            Actions.times += 1
            self.OnAction()