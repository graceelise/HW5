from microbit import *
import math
step1 = Image("00000:"
              "00000:"
              "00900:"
              "00000:"
              "00000")

step2 = Image("00000:"
              "09090:"
              "00900:"
              "00000:"
              "00000")
step3 = Image("00000:"
              "09090:"
              "09990:"
              "00900:"
              "00000")
step4 = Image.HEART_SMALL
step5 = Image.HEART
#i = 0

stepList = [step1,step2,step3,step4,step5]

if(button_a.is_pressed()):
    while True:
        for x in range(0,4,1):
            display.show(stepList)
            sleep(1000)
        if(button_b.is_pressed()):
            display.clear


