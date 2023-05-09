# esp32收到指令 进行功能分发
import main_func
from machine import soft_reset
def main(data):
    if(data=="前进开始"):
        main_func.front(True)
    elif(data=="前进停止"):
        main_func.front(False)
    elif(data=="后退开始"):
        main_func.back(True)
    elif(data=="后退停止"):
        main_func.back(False)
    elif(data=="向左开始"):
        main_func.left(True)
    elif(data=="向左停止"):
        main_func.left(False)
    elif(data=="向右开始"):
        main_func.right(True)
    elif(data=="向右停止"):
        main_func.right(False)
    elif(data=="autoMode"):
        main_func.autoMode()
    elif(data=="manualMode"):
        main_func.manualMode()
    elif(data=="小车已经离线"):
        soft_reset()
    elif(data.startswith("设置速度")):
        v = int(data[4:])
        main_func.sp.setSpeed(v)
