'''
author : Febi Mudiyanto
date   : 03-04-2021

desc   : Run Program, kemudian tempatkan kursor di aplikasi Growtopia

'''


import pyautogui
import time
import random

def punch():
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
def clicking():
    pyautogui.click(clicks=8,  interval=0.25)


def back_left():
    pyautogui.keyDown('left')
    time.sleep(10)
    pyautogui.keyUp('left')
    
def back_right():
    pyautogui.keyDown('right')
    time.sleep(10)
    pyautogui.keyUp('right')

def tambang(arah='left'):
    punch()
    move(arah)

    time.sleep(random.random()+0.2)
    punch()
    move(arah)


time.sleep(2)
state_mouse=pyautogui.position()
i=0
while(i<100 and (state_mouse == pyautogui.position()) ):
    #tambang('right')
    clicking()
    punch()
    move('right')
    move('right')
    print(i)
    i+=1


pyautogui.alert('Selesai')

