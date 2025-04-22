'''
This is a practice script, I want to do an autoclicker
I like to play minecraft but during work hours I tend to be AFK
So the plan is to do a script that makes steve jump every 25 minutes to avoid getting disconnected for idleing
'''

'''
proyect aborted, the script works everywhere except for minecraft
I'm going to try again in the future
'''
import time
import pyautogui

def press_space():
    pyautogui.press('space')  
while True:
    press_space()  
    print(f"Space bar pressed at - {time.strftime('%H:%M:%S')}") 
    time.sleep(1)      