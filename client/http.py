from machine import Pin, idle
from network import WLAN, STA_IF
import usocket
import ujson
import urequests
from utime import sleep

from secrets import ssid, ssidpassword
import settings

led = Pin(2, Pin.OUT)
# receiveBuffer = 4096
receiveBuffer = 8192

def updateJSON(json):
    led.off()

    if type(json) is dict:
        json = ujson.dumps(json) # To JSON string

    json = json.replace(": ", ":")  # Remove spaces from string
    json = json.replace(", ", ",")  # Remove spaces from string
    json = json.replace(" ", "%20") # Spaces to url encoding

    req = urequests.get(settings.apiUrl + "&edit=" + json)
    print("Server response: %s" % req.text)
    req.close()

    led.on()


def getJSON():
    led.off()

    r = urequests.get(settings.apiUrl)
    ret = r.json()
    r.close()

    led.on()
    return ret


def wifi_connect():
    led.off()
    wlan = WLAN(STA_IF)
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid, ssidpassword)

        while not wlan.isconnected():
            idle()
            pass
    # print('Network secrets:', sta_if.ifconfig())
    led.on()
