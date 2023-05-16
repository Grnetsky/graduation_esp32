from machine import Pin, ADC  #引入ADC模块
from time import sleep

def getPpercent():
    pot = ADC(Pin(34))         #定义34脚为ADC脚(在32~39上可用)，可以读取模拟电压
    pot.width(ADC.WIDTH_12BIT) #读取的电压转为0-4096；ADC.WIDTH_9BIT：0-511
    pot.atten(ADC.ATTN_11DB)   #衰减设置范围：输入电压0-3.3v
    pot_value = pot.read() //4  #使读取的电压变为0-1024
    p_percent = int(pot_value / 180 * 100) # 剩余电量百分比
    if(p_percent>100):
        p_percent=100
    return p_percent
    
