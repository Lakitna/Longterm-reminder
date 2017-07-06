from machine import Pin
from utime import sleep_us

class Button:
    def __init__(self, p, iterations):
        self._pin = Pin(p, Pin.IN, Pin.PULL_UP)
        self.val = 1
        self._valA = 1
        self._valB = 1
        self._readings = iterations

    def up(self):
        if self._valB < self._valA:
            return True
        else:
            return False

    def down(self):
        if self._valB > self._valA:
            return True
        else:
            return False

    def poll(self):
        # Read button state and make sure it's not bouncing
        tmp = 0
        for i in range(0, self._readings):
            tmp += self._pin.value()
            sleep_us(1)

        if tmp == self._readings:
            self._valB = self._valA
            self._valA = 1
            self.val = True
            return 1
        elif tmp == 0:
            self._valB = self._valA
            self._valA = 0
            self.val = False
            return 0
