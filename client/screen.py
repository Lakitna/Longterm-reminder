import utime as time
from machine import Pin, I2C
from sh1106 import SH1106_I2C
import framebuf
import icons

class Screen:
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
    lineHeight = 10

    def __init__(self):
        self.w = 128
        self.h = 64

        self.oled = SH1106_I2C(self.w, self.h, self.i2c, Pin(16), 0x3c)
        self.oled.init_display()

        self.fps = 0
        self.fps_sec_prev = 0
        self.fps_c = 0
        self.fps_new_sec = False
    # print( i2c.scan() )

    def fpsPoll(self):
        sec = time.time()
        if sec == self.fps_sec_prev:
            self.fps_c += 1
            self.fps_new_sec = False
        else:
            self.fps = self.fps_c
            self.fps_c = 0
            self.fps_sec_prev = sec
            self.fps_new_sec = True

    def text(self, txt, x=0, y=0, repl=False):
        txt = txt.split('\n')

        for i in range(0,len(txt)):
            self.oled.text(txt[i], x, (y + (self.lineHeight*i)), 2)

        if repl:
            print(txt)

    def icon(self, id, x=0, y=0):
        fb = framebuf.FrameBuffer(icons.get(id), 32, 32, framebuf.MVLSB)
        self.oled.framebuf.blit(fb, x, y)

    def rect(self, x, y, w, h):
        self.oled.fill_rect(x,y,w,h,1)

    def line(self, x1, y1, x2, y2):
        self.oled.line(x1, y1, x2, y2, 1)

    def clear(self):
        self.oled.fill(0)

    def sleep(self, state):
        self.oled.sleep(state)

    def show(self):
        self.oled.show()
