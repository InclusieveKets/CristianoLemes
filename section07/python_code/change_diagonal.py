from sense_hat import SenseHat
import time
import random
random.seed()

sense = SenseHat()
sense.set_rotation(270)

msleep = lambda x: time.sleep(x / 1000.0)

B = (0, 0, 0)
w = (255, 255, 255)
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
colors = (r, g, b, w)
#colors = ([255, 0, 0], [255, 0, 0], [255, 87, 0], [255, 196, 0], [205, 255, 0], [95, 255, 0], [0, 255, 13], [0, 255, 122],
#    [255, 0, 0], [255, 96, 0], [255, 205, 0], [196, 255, 0], [87, 255, 0], [0, 255, 22], [0, 255, 131], [0, 255, 240],
#    [255, 105, 0], [255, 214, 0], [187, 255, 0], [78, 255, 0], [0, 255, 30], [0, 255, 140], [0, 255, 248], [0, 152, 255],
#    [255, 223, 0], [178, 255, 0], [70, 255, 0], [0, 255, 40], [0, 255, 148], [0, 253, 255], [0, 144, 255], [0, 34, 255],
#    [170, 255, 0], [61, 255, 0], [0, 255, 48], [0, 255, 157], [0, 243, 255], [0, 134, 255], [0, 26, 255], [83, 0, 255],
#    [52, 255, 0], [0, 255, 57], [0, 255, 166], [0, 235, 255], [0, 126, 255], [0, 17, 255], [92, 0, 255], [201, 0, 255],
#    [0, 255, 66], [0, 255, 174], [0, 226, 255], [0, 117, 255], [0, 8, 255], [100, 0, 255], [210, 0, 255], [255, 0, 192],
#    [0, 255, 183], [0, 217, 255], [0, 109, 255], [0, 0, 255], [110, 0, 255], [218, 0, 255], [255, 0, 183], [255, 0, 74])
list_diagonals = ( 0,  1,  2,  3,  4,  5,  6, 7,
                  15, 23, 31, 39, 47, 55, 63)

pixels = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
]

def update_diagonal(ini, c):
  if ini == 0 or ini == 63:
    pixels[ini] = c
    return
  elif ini == 1 or ini == 55:
    shift = 2
  elif ini == 2 or ini == 47:
    shift = 3
  elif ini == 3 or ini == 39:
    shift = 4
  elif ini == 4 or ini == 31:
    shift = 5
  elif ini == 5 or ini == 23:
    shift = 6
  elif ini == 6 or ini == 15:
    shift = 7
  elif ini == 7:
    shift = 8
  pos = ini
  for i in range(shift):
    pixels[pos+(7*i)] = c

def update_pixels(lenght):
  for i in range(lenght+1):
    next_d = list_diagonals[i%len(list_diagonals)]
    c = colors[i%len(colors)]
    update_diagonal(next_d, c)

for i in range(30):
  update_pixels(i)
  sense.set_pixels(pixels)
  time.sleep(0.5)