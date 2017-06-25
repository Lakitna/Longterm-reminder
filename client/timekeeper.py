from utime import ticks_ms, ticks_diff

class TimeKeeper:
    minute_ms = 60000

    def __init__(self, year, month, day, hour, minute):
        self.Y = year
        self.M = month
        self.D = day
        self.h = hour
        self.m = minute
        self._ms_prev = 0

    def poll(self):
        now = ticks_ms()
    	if ticks_diff(now, self._ms_prev) > self.minute_ms:
            self.m += 1
            if self.m >= 60:
                self.h += 1
                self.m = 0
                if self.h >= 24:
                    self.D += 1
                    self.h = 0

            print(self.get_stamp())
            self._ms_prev += self.minute_ms

    def set(self, year, month, day, hour, minute):
        self.Y = year
        self.M = month
        self.D = day
        self.h = hour
        self.m = minute

    def get_stamp(self):
        return "%d-%d-%d %d:%d" % (self.Y, self.M, self.D, self.h, self.m)
