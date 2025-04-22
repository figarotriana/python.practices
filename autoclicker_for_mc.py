'''
This is a practice script, I want to do an autoclicker
I like to play minecraft but during work hours I tend to be AFK
So the plan is to do a script that makes steve jump every 25 minutes to avoid getting disconnected for idleing
'''
import time
import pyautogui

def press_space():
    pyautogui.press('space')  # Simula la pulsación de la barra espaciadora

while True:
    press_space()  # Simula la pulsación
    print(f"Space bar pressed at {time.strftime('%H:%M:%S')}")
    time.sleep(1)  