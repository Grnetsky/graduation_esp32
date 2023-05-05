# 功能代码
from machine import Pin
# 左轮
p12 = Pin(12,Pin.OUT)
p14 = Pin(14,Pin.OUT)

# 右轮
p27 = Pin(27,Pin.OUT)
p26 = Pin(26,Pin.OUT)

"""前进"""
def front(state):
    if(state):
        print("小车向前开始")
        p12.on()
        p14.off()
        
        p26.on()
        p27.off()
    else:
        print("小车向前结束")
        p12.off()
        p26.off()

"""后退"""
def back(state):
    if(state):
        print("小车后退开始")
        p12.off()
        p14.on()
        
        p26.off()
        p27.on()
    else:
        print("小车后退结束")
        p14.off()
        p27.off()

"""向左"""
def left(state):
    if(state):
        print("小车向左开始")
        p12.off()
        p14.off()

        p26.on()
        p27.ff()
    else:
        print("小车向左结束")
        p26.off()

"""向右"""
def right(state):
    if(state):
        print("小车向右开始")
        p12.on()
        p14.off()
        
        p26.off()
        p27.off()
    else:
        print("小车向右结束")
        p12.off()
