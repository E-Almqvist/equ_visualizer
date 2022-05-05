#!/usr/bin/python

#from manim import *
import pygame 
from equation import *
from render import *

#class FunnelScene(Scene):
#    def construct(self):
#        cir = Circle()
#        sq = Square()
#
#        self.play(Create(sq))
#        self.play(Transform(sq, cir))
#        self.play(FadeOut(sq))

equ = Function( lambda x,y: x**2 + y, 2 )
equ_der = Function( lambda x,y: 2*x + 1, 2 )

my_ode = ODE([equ, equ_der])

points = []
for i in range(0, 100):
    points.append(my_ode.get_point(i, i))

space = RenderSpace()

point_objs = []
for p in points:
    point_objs.append( Point_2D(space, p[0], p[1]) )

space.points = point_objs
space.render()
