# 红外模块
from machine import PWM,Pin
red=Pin(32,Pin.OUT)#
import utime
receive=Pin(33,Pin.IN)
red.value(1)
print(red.value())
print(receive.value())
while True:
    if receive.value():
      print(receive.value())
    else:
      print("no")
    
    utime.sleep(0.5)