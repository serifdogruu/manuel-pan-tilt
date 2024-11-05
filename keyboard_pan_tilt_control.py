#imports
import time
import keyboard
from pyfirmata import Arduino, SERVO
#board
board = Arduino('COM4')
# attach pins and modes
pin_9 = board.digital[9]
pin_9.mode = SERVO

pin_5 = board.digital[5]
pin_5.mode = SERVO
#first angle and change rate (crt)
angle = 90
crt = 5

while True:

    if keyboard.is_pressed('d'): #right
        if angle - crt > 0:
            angle = angle - crt
            pin_5.write(angle),
            time.sleep(0.1)

    elif keyboard.is_pressed('a'): #left
        if angle + crt < 180:
            angle = angle + crt
            pin_5.write(angle)
            time.sleep(0.1)

    elif keyboard.is_pressed('w'): #up
        if angle - crt > 0:
            angle = angle - crt
            pin_9.write(angle)
            time.sleep(0.1)

    elif keyboard.is_pressed('s'): #down
        if angle + crt < 180:
            angle = angle + crt
            pin_9.write(angle)
            time.sleep(0.1)

    elif keyboard.is_pressed('t'):  #increase change rate
        if crt + 1 < 180:
            crt = crt + 1
            time.sleep(0.1)


    elif keyboard.is_pressed('r'):  #reset
        angle = 90
        crt = 5
        pin_9.write(angle)
        time.sleep(0.1)


    elif keyboard.is_pressed('esc'):
        break