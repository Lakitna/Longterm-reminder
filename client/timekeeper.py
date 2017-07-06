import utime as time

class TimeKeeper:
    def __init__(self, year, month, day, hour, minute, second=0):
        self.Y = year
        self.M = month
        self.D = day
        self.h = hour
        self.m = minute
        self.s = second
        self._sec_prev = 0

    def poll(self):
        now = time.time()
    	if now != self._sec_prev:
            self.s += 1
            if self.s >= 60:
                self.m += 1
                self.s = 0
                if self.m >= 60:
                    self.h += 1
                    self.m = 0
                    if self.h >= 24:
                        self.D += 1
                        self.h = 0

            self._sec_prev = now

    def set(self, year, month, day, hour, minute, second=0):
        self.Y = year
        self.M = month
        self.D = day
        self.h = hour
        self.m = minute
        self.s = second

    def get_stamp(self):
        Y = self.Y - 2000 # Make shorthand year
        return "%s-%d-%d %d:%d:%d" % (Y, self.M, self.D, self.h, self.m, self.s)

    def get_obj(self):
        return {'y': self.Y, 'm': self.M, 'd': self.D}
