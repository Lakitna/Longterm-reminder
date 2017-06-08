import time
import machine
import gfx
import PCD8544 as LCD
# import Nokia_5110 as display
# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont

SPI = machine.SPI


# Software serial pin setup
SCLK = 16
DIN = 14
DOUT = 0
DC = 12
RST = 15
CS = 13


print(dir(LCD))
# disp = display.PCD8544(DC, RST, SCLK, DIN, CS)
# disp = display.Adafruit_PCD8544(SCLK, DIN, DC, RST, CS)

# software SPI usage:
disp = LCD.PCD8544(DC, RST, SCLK, DIN, DOUT, CS)

# Software SPI usage (defaults to bit-bang SPI interface):
#disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

#
# # Draw a white filled box to clear the image.
# draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
#
# # Draw some shapes.
# draw.ellipse((2,2,22,22), outline=0, fill=255)
# draw.rectangle((24,2,44,22), outline=0, fill=255)
# draw.polygon([(46,22), (56,2), (66,22)], outline=0, fill=255)
# draw.line((68,22,81,2), fill=0)
# draw.line((68,2,81,22), fill=0)
#
# disp.display()

# print('Press Ctrl-C to quit.')
# while True:
# 	time.sleep(1.0)
