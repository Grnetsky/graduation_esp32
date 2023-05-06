# 红外模块
from machine import PWM,Pin
import utime


red=Pin(32,Pin.OUT)#
receive=Pin(33,Pin.IN)
red.value(1)


def main(red,receive):
    print(red.value())
    print(receive.value())
    while True:
        if receive.value():
            # 黑色
            print("是黑色")
        else:
            # 其他颜色
            
            pass
        utime.sleep(0.5)
