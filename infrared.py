import machine
import time
import main_func
sensor_pin1_en = machine.Pin(32, machine.Pin.OUT)
sensor_pin1 = machine.Pin(33, machine.Pin.IN)
sensor_pin1_en.on()

sensor_pin2_en = machine.Pin(19, machine.Pin.OUT)
sensor_pin2 = machine.Pin(21, machine.Pin.IN)
sensor_pin2_en.on()

# 设置速度
main_func.sp.setSpeed(30)
# 主循环
while True:
    sensor_value1 = sensor_pin1.value()
    sensor_value2 = sensor_pin2.value()

    # 当两个传感器都检测到黑线时，小车直行
    if sensor_value1 == 0 and sensor_value2 == 0:
        main_func.front(True)  # 直行
    # 当左边的传感器检测到黑线时，小车左转
    elif sensor_value1 == 1:
        main_func.left(True)
        main_func.right(False)# 左转
        main_func.front(False)
    # 当右边的传感器检测到黑线时，小车右转
    elif sensor_value2 == 1:
        main_func.right(True)
        main_func.left(False)# 左转
        main_func.front(False)  # 右转
    else:
        main_func.stop()

    time.sleep(0.1)  # 延迟一段时间，可以调整延迟时间来控制小车的运动速度