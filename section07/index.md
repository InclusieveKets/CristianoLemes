---
layout: default
title: Section 07 - Python
---

# Python

The class was hosted again by Zoom and it was talked about the bases to develop Python programs.
It was presented a little bit of the history of this programming language that has been used a lot in several fields, specially in academic field.
Researchers have been using this language and its facilities to design their experiments and to generate the report data of their results.
With the grow of this language, it becames very powerful and you can do a lot with the language using the modules provided by several third party programers.
You can even find packages with machine learning algorithms which is very useful in several fields of academic and industry nowadays.
And one of the advantages is that you can design code without even install python in your computer.
Bellow you can find several links that you can use to design python code using cloud computing.

One of the example designed in the class, I have designed a code to change the diagonal of the AstroPi Vis (trinket.io) with different colors changing the entirely diagonal with the current color.
It was used the sense_hat module to design this program.
It could use other sensors too, such as temperature and humidity.
Bellow you can see the code of this simple example.

```python
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
```

## Websites

* [Colab Google](https://colab.research.google.com/)
* [Trinket](https://trinket.io/)
* [Create.withcode](https://create.withcode.uk/)
* [Sense Hat Examples](https://github.com/astro-pi/python-sense-hat/blob/master/examples/README.md)
* [OpenCV modules](https://docs.opencv.org/master/)