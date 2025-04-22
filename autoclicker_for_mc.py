'''
This is a practice script, I want to do an autoclicker
I like to play minecraft but during work hours I tend to be AFK
So the plan is to do a script that makes steve jump every 25 minutes to avoid getting disconnected for idleing
'''
import keyboard
import time

Wait_time = 2
Hour = time.strftime("%H:%M:%S")

while True:
    if keyboard.is_pressed('esc'):
        print("STOPPED")
        break
    #so it doesn't repeat forever
    
    time.sleep(Wait_time)
    keyboard.press_and_release('space')
    print ("space bar at " + time.strftime("%H:%M:%S"))
      