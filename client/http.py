from secrets import ssid, ssidpassword
from machine import Pin, idle
from network import WLAN, STA_IF
import usocket
import ujson
import urequests
from utime import sleep


led = Pin(2, Pin.OUT)
# receiveBuffer = 4096
receiveBuffer = 8192

def updateJSON(url, json):
    led.off()

    if type(json) is dict:
        json = ujson.dumps(json) # To JSON string

    json = json.replace(": ", ":")  # Remove spaces from string
    json = json.replace(", ", ",")  # Remove spaces from string
    json = json.replace(" ", "%20") # Spaces to url encoding

    req = urequests.get(url + "&edit=" + json)
    print("Server response: %s" % req.text)
    req.close()

    led.on()


def getJSON(url):
    led.off()

    r = urequests.get(url)
    ret = r.json()
    r.close()

    led.on()
    return ret


def http_request(url, method='GET'):
    _, _, host, path = url.split('/', 3)
    addr = usocket.getaddrinfo(host, 80)[0][-1]
    s = usocket.socket()
    s.connect(addr)
    s.send(bytes('%s /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (method, path, host), 'utf8'))

    ret = s.recv(receiveBuffer)

    s.close()
    return ret


def do_connect():
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
