import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.GP25, 1)

while True:
    pixels.fill((85, 57, 204))
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)