from machine import ADC
from utime import ticks_ms, ticks_diff, sleep_us

class Analog:
    def __init__(self, p, iterations):
        self._pin = ADC(p)
        self._ms_prev = ticks_ms()
        self._counter = 0
        self._val_sum = 0
        self._readings = iterations

        self.val = 0
        self.val_period = 0

    def poll(self):
        tmp = 0
        for i in range(0, self._readings):
            tmp += self._pin.read()
            sleep_us(1)

        self.val = int( tmp / self._readings )
        return self.val

    def poll_period(self, seconds):
        # Poll every second and return the average after [input parameter] seconds
        now = ticks_ms()
        ret = False
        if ticks_diff(now, self._ms_prev) > 1000:
            # self._val_sum += self.poll()
            self._val_sum += self.poll() * (1/seconds)

            self._counter += 1
            if self._counter >= seconds:
                # ret = int(self._val_sum / self._counter)
                ret = self._val_sum
                self.val_period = self._val_sum

                self._val_sum = 0
                self._counter = 0

            self._ms_prev = now
        return ret
