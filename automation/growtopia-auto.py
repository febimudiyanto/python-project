'''
author : Febi Mudiyanto
date   : 03-04-2021

desc   : Run Program, kemudian tempatkan kursor di aplikasi Growtopia

'''


import pyautogui
import time
import random

def back_left():
    pyautogui.keyDown('left')
    time.sleep(15)
    pyautogui.keyUp('left')
    
def back_right():
    pyautogui.keyDown('right')
    time.sleep(15)
    pyautogui.keyUp('right')

def tambang(arah='left'):
    def clicking():
        pyautogui.keyDown('x')
        time.sleep(3)
        pyautogui.keyUp('x')

    def move(arah):
        pyautogui.keyDown(arah)
        if arah=='right':
            time.sleep(0.055)
        else:
            time.sleep(0.06)
        pyautogui.keyUp(arah)

    time.sleep(random.random()+0.2)
    clicking()
    move(arah)


time.sleep(2)
i=0
while(i<60):
    tambang('left')
    print(i)
    i+=1
back_right()


pyautogui.alert('Selesai')
