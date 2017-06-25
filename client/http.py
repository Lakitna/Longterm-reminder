from secrets import ssid, ssidpassword
from machine import Pin
from network import WLAN, STA_IF
import usocket
import ujson


led = Pin(2, Pin.OUT)
receiveBuffer = 4096


def updateJSON(url, json):
    led.off()

    response = http_request(url + "&edit=" + json)
    response = str(response, 'utf8')
    response = response.split('\r\n\r\n', 1)[1]

    print("Server response: %s" % response)

    led.on()


def getJSON(url):
    led.off()

    response = http_request(url)
    data = str(response, 'utf8')       # Encoding casting
    data = data.split('\r\n\r\n', 1)[1] # Strip HTTP headers
    data = ujson.loads(data)           # Convert to JSON

    led.on()
    return data


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
    sta_if = WLAN(STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, ssidpassword)
        while not sta_if.isconnected():
            pass
    print('(\(^_^)/) Success')
    # print('Network secrets:', sta_if.ifconfig())
    led.on()
