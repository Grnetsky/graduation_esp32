# 功能代码
from machine import Pin,PWM
# 左轮
print("初始化")
p12 = PWM(Pin(12),freq=1000)
p14 = PWM(Pin(14),freq=1000)

# 右轮
p27 = PWM(Pin(27),freq=1000)
p26 = PWM(Pin(26),freq=1000)

class Speed():
    s = 512
    
    def getSpeed(self):
        return self.s
    
    def setSpeed(self,value):
        self.s = value*10
sp = Speed() 

    
"""前进"""

def front(state):
    if(state):
        print("小车向前开始 速度：",sp.getSpeed())
        p12.duty(sp.getSpeed())
        p14.duty(0)
        
        p26.duty(sp.getSpeed())
        p27.duty(0)
    else:
        print("小车向前结束")
        p12.duty(0)
        p26.duty(0)

"""后退"""
def back(state):
    if(state):
        print("小车后退开始")
        p12.duty(0)
        p14.duty(sp.getSpeed())
        
        p26.duty(0)
        p27.duty(sp.getSpeed())
    else:
        print("小车后退结束")
        p14.duty(0)
        p27.duty(0)

"""向左"""
def left(state):
    if(state):
        print("小车向左开始")
        p12.duty(0)
        p14.duty(0)

        p26.duty(sp.getSpeed())
        p27.duty(0)
    else:
        print("小车向左结束")
        p26.duty(0)

"""向右"""
def right(state):
    if(state):
        print("小车向右开始")
        p12.duty(sp.getSpeed())
        p14.duty(0)
        
        p26.duty(0)
        p27.duty(0)
    else:
        print("小车向右结束")
        p12.duty(0)
