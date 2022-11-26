from gl import Renderer, _color_, V2, V3
from textures import Texture
from obj import Obj
import struct
from collections import namedtuple
import sys
#################################
sys.setrecursionlimit(5000)
width = 1300
height = 866
depth = -10
black = _color_(0, 0, 0)
white = _color_(1, 1, 1)
borderColor = (0.8, 0.6, 0.2)
fillingColor = (0.4, 0.7, 0.3)
rend = Renderer(width, height)
rend.glClearColor(0, 0, 0)
rend.glClear()
rend.glColor(0.8, 0.6, 0.2)


p1 = [V2(165, 380), V2(185, 360), V2(180, 330), V2(207, 345),
      V2(233, 330), V2(230, 360), V2(250, 380), V2(220, 385),
      V2(205, 410), V2(193, 383)]

p2 = [V2(321, 335), V2(288, 286), V2(339, 251), V2(374, 302)]

p3 = [V2(377, 249), V2(411, 197), V2(436, 249)]

p4 = [V2(413, 177), V2(448, 159), V2(502, 88), V2(553, 53), V2(535, 36), V2(676, 37), V2(660, 52), V2(750, 145), V2(761, 179), V2(
    672, 192), V2(659, 214), V2(615, 214), V2(632, 230), V2(580, 230), V2(597, 215), V2(552, 214), V2(517, 144), V2(466, 180)]

p5 = [V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)]

rend.glDraw(p1)
rend.glFill(p1)

rend.glColor(0.4, 0.6, 0.1)
rend.glDraw(p2)
rend.glFill(p2)

rend.glColor(0.7, 0.1, 0.2)
rend.glDraw(p3)
rend.glFill(p3)

rend.glColor(0.8, 0.1, 0.1)
rend.glDraw(p4)
rend.glFill(p4)

rend.glColor(0.1, 0.4, 0.9)
rend.glDraw(p5)
rend.glFill(p5)

rend.write("LAB1.bmp")
