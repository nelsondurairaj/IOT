#import necessary libraries
from machine import Pin
import utime

#set pin 28 as output in led variable
led = Pin(28, Pin.OUT)
#set led to low
led.low()

#loop forever
while True:
    #toggle led
    led.toggle()
    #while toggling print toggle
    print("Toggle")
    #wait for 1 second then repeat
    utime.sleep(1)