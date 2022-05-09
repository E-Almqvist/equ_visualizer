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

#equ = Function( lambda x,y: math.sin(2*x) - y, 2 )
#equ_der = Function( lambda x,y: 2*math.cos(2*x) - 2*math.sin(2*y), 2 )
equ1 = Function( lambda x, v: v, 2)
equ2 = Function( lambda x, v: -2*x - 0.2*v, 2 )

my_ode = ODE([equ1, equ2])

print("Composing points... ")
points = []
points.append( [100, 100] ) # start point
num_points = 1600
delta = 0.00001
for i in range(1, num_points):
    print(f"{round(i*100/num_points, 2)}%", end="\r")
    dx, dy = points[i-1]
    dx += delta
    dy += delta
    points.append( my_ode.get_point(dx, dy) )

space = RenderSpace()

point_objs = []
for p in points:
    print(f"{p[0]} {p[1]}")
    point_objs.append( Point_2D(space, p[0], p[1], (25, 255, 25)) )

space.points = point_objs
space.render(0.00000000000000000001)
