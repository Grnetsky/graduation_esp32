# 功能代码
from machine import Pin

p12 = Pin(12,Pin.OUT)
p14 = Pin(14,Pin.OUT)

"""前进"""
def front(state):
    if(state):
        print("小车向前开始")
        p12.value(0)
        p14.value(1)
    else:
        print("小车向前结束")
        p14.value(0)

"""后退"""
def back(state):
    pass

"""向左"""
def left(state):
    pass

"""向右"""
def right(state):
    pass