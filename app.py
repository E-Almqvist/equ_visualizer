#!/usr/bin/python

#from manim import *
import pygame 
from equation import *
from render import *
import math
import numpy as np

#class FunnelScene(Scene):
#    def construct(self):
#        cir = Circle()
#        sq = Square()
#
#        self.play(Create(sq))
#        self.play(Transform(sq, cir))
#        self.play(FadeOut(sq))

equ = Function( lambda x,y: math.sin(2*x) + y, 2 )
equ_der = Function( lambda x,y: x+y, 2 )

my_ode = ODE([equ, equ_der])

print("Composing points... ")
points = []
num_points = 1600
for i in np.arange(0, num_points, 0.01):
    points.append(my_ode.get_point(i, i))

space = RenderSpace()

point_objs = []
for p in points:
    point_objs.append( Point_2D(space, p[0], p[1], (255-p[1], p[0], p[1])) )

space.points = point_objs
space.render(10)
