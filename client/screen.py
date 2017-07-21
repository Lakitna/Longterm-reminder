import utime as time
from machine import Pin, I2C
from sh1106 import SH1106_I2C
import framebuf
import icons
from httpUpdate import activeReminders
import inputs
import settings

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

    def text(self, txt, x=0, y=0, w=0, repl=False):
        if w>0:
            txt = txt.replace("-", "-\n")
        else:
            txt = txt.replace("-", "")

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

    def pixel(self, x, y):
        self.oled.pixel(x, y, 1)

    def clear(self):
        self.oled.fill(0)

    def sleep(self, state):
        self.oled.sleep(state)

    def show(self):
        self.oled.show()




oled = Screen()

def statusShow(id):
    oled.clear()
    if id == 0:
        oled.icon('wifi', 48, 10)
        oled.text("Connecting", 24, 44, 0, True)
    elif id == 1:
        oled.icon('wifi', 48, 10)
        oled.text("Success", 36, 44, 0, True)
    oled.show()


def build(response):
    oled.fpsPoll() # Count frames
    oled.clear() # Clear display

    # Build display
    if len(activeReminders) == 0:
    	# Set display sleep state
    	oled.sleep(True)
    else:
    	# Set display sleep state
    	if inputs.ldr_A.val_period < settings.ldrMinValue:
    		oled.sleep(True)
    	else:
    		oled.sleep(False)

    	# Different screens for different amount of active reminders
    	if len(activeReminders) == 1:
            node = activeReminders[ next(iter(activeReminders)) ]
            descr = node['descr']
            oled.icon(node['icon'], 48, 0)
            oled.text(descr, (64 - ( len(descr) * 4 )), 36, 0) # Center aligned

    	elif len(activeReminders) >= 2:
            iterate = iter(activeReminders)

    		# Left column
            node = activeReminders[ next(iterate) ]
            descr = node['descr']
            oled.icon(node['icon'], 16, 0)
            oled.text(descr, 0, 36, 1) # Left aligned

            # oled.line(64,0, 64,64)
            for i in range(0,16):
                oled.pixel(64, i*4)

            # Right column
            node = activeReminders[ next(iterate) ]
            descr = node['descr']
            oled.icon(node['icon'], 80, 0)
            oled.text(descr, 66, 36, 1) # Left aligned


        # Show FPS counter
    	oled.text(str(oled.fps), 0, 0)

    	# Button state rectangles
    	if inputs.but_A.val == 1:
    		oled.rect(107, 62, 10, 2)
    	else:
    		oled.text(str(inputs.ldr_A.val_period), 104, 52)
    	if inputs.but_B.val == 1:
    		oled.rect(118, 62, 10, 2)

    	oled.show()
