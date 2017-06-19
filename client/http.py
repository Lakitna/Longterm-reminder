import network
import socket
import machine
import ujson
import secrets


led = machine.Pin(2, machine.Pin.OUT)
receiveBuffer = 4096
connectSsid = secrets.ssid
connectPass = secrets.ssidpassword


def updateJSON(url, json):
    led.low()

    response = http_request(url + "&edit=" + json)

    led.high()


def getJSON(url):
    led.low()

    response = http_request(url)
    data = str(response, 'utf8')       # Encoding casting
    data = '{' + data.split('{', 1)[1] # Strip HTTP headers
    data = ujson.loads(data)           # Convert to JSON

    led.high()
    return data


def http_request(url, method='GET'):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('%s /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (method, path, host), 'utf8'))

    ret = s.recv(receiveBuffer)
    s.close()
    return ret


def do_connect():
    led.low()
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(connectSsid, connectPass)
        while not sta_if.isconnected():
            pass
    print('Success')
    # print('Network secrets:', sta_if.ifconfig())
    led.high()
