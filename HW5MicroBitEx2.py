# I did this by myself
from microbit import *

x = 0
y = 0

for z in range(1,16,1):
    while x < 4:
        display.set_pixel(x,y,9)
        sleep(300)
        x = x + 1
    while y < 4 and x == 4:
        display.set_pixel(x,y,9)
        sleep(300)
        y = y + 1
    while y == 4 and x > 0:
        display.set_pixel(x,y,9)
        sleep(300)
        x = x - 1
    while x == 0 and y > 0:
        display.set_pixel(x,y,9)
        sleep(300)
        y = y - 1