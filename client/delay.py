from utime import ticks_ms, ticks_diff, sleep_ms

class Delay:
    def __init__(self, ms):
        self._ms_prev = 0
        self.mseconds = ms

    def noSleep(self):
    	now = ticks_ms()
    	# If interval passed or on first loop
    	if ticks_diff(now, self._ms_prev) > self.mseconds:
            self._ms_prev = now
            return True
        else:
            return False

    def sleep(self):
        sleep_ms(self.mseconds)

    def setTime(self, ms):
        self.mseconds = ms
