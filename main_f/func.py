import network as net
import uasyncio as a
import json
from random import randint
from machine import Pin,soft_reset
import gc
import main_func
from async_websocket_client import AsyncWebsocketClient
import dispatchFunc
from upload import uploadData
# trying to read config --------------------------------------------------------
# if config file format is wrong, exception is raised and program will stop
print("Trying to load config...")

f = open("../config.json")
text = f.read()
f.close()
config = json.loads(text)
del text
# ------------------------------------------------------------------------------

print("Create WS instance...")
# create instance of websocket
ws = AsyncWebsocketClient(config['socket_delay_ms'])

print("Created.")

# this lock will be used for data interchange between loops --------------------
# better choice is to use uasynio.queue, but it is not documented yet
lock = a.Lock()
# this array stores messages from server
data_from_ws = []
# ------------------------------------------------------------------------------

# SSID - network name
# pwd - password
# attempts - how many time will we try to connect to WiFi in one cycle
# delay_in_msec - delay duration between attempts
async def wifi_connect(SSID: str, pwd: str, attempts: int = 3, delay_in_msec: int = 200) -> network.WLAN:
    wifi = net.WLAN(net.STA_IF)

    wifi.active(1)
    count = 1

    while not wifi.isconnected() and count <= attempts:
        print("WiFi connecting. Attempt {}.".format(count))
        if wifi.status() != net.STAT_CONNECTING:
            wifi.connect(SSID, pwd)
        await a.sleep_ms(delay_in_msec)
        count += 1

    if wifi.isconnected():
        print("ifconfig: {}".format(wifi.ifconfig()))
    else:
        print("Wifi not connected.")

    return wifi

# Function for main control loop.
# It makes sense for ESP32 with integrated LED on Pin2.
# Write another function for main loop for other controller types.
p2 = Pin(2, Pin.OUT)
async def blink_sos():
    global p2

    async def blink(on_ms: int, off_ms: int):
        p2.on()
        await a.sleep_ms(on_ms)
        p2.off()
        await a.sleep_ms(off_ms)

    await blink(1000, 50)
    await blink(200, 50)
    await blink(200, 50)
    await blink(400, 50)
    await blink(400, 50)
    await blink(400, 50)
    await blink(200, 50)
    await blink(200, 50)
    await blink(200, 50)

# ------------------------------------------------------
# Main loop function: blink and send data to server.
# This code emulates main control cycle for controller.
async def blink_loop():
    global lock
    global data_from_ws
    global ws

    # Main "work" cycle. It should be awaitable as possible.
    while True:
        await blink_sos()
        if ws is not None:
            if await ws.open():
                await ws.send('SOS!')
                await ws.send(uploadData())
            print("SOS!", end=' ')
                
            # lock data archive
            await lock.acquire()
            if data_from_ws:
                for item in data_from_ws:
                    print("\nData from ws: {}".format(item))
                    print(item)
                    if(item=='手机已连接'):
                        await ws.send("ok")
                data_from_ws = []
            lock.release()
            gc.collect()

        await a.sleep_ms(400)
# ------------------------------------------------------


# ------------------------------------------------------
# Task for read loop
async def read_loop():
    global config
    global lock
    global data_from_ws

    # may be, it
    wifi = await wifi_connect(config["wifi"]["SSID"], config["wifi"]["password"])
    while True:
        gc.collect()
        if not wifi.isconnected():
            wifi = await wifi_connect(config["wifi"]["SSID"], config["wifi"]["password"])
            if not wifi.isconnected():
                await a.sleep_ms(config["wifi"]["delay_in_msec"])
                continue
        try:
            print("Handshaking...")
            # connect to test socket server with random client number
            if not await ws.handshake("{}{}".format(config["server"], config["sid"])):
                raise Exception('Handshake error.')
            print("...handshaked.")

            mes_count = 0
            while await ws.open():
                data = await ws.recv()
                print("Data: " + str(data) + "; " + str(mes_count))
                # 每十秒断开一次
                dispatchFunc.main(data)
                if data is not None:
                    await lock.acquire()
                    data_from_ws.append(data)
                    lock.release()

                await a.sleep_ms(50)
        except Exception as ex:
            print("Exception: {}".format(ex))
            # 能否断线重连?
            await a.sleep(1)
# ------------------------------------------------------
