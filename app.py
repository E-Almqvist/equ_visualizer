#!/usr/bin/python

#from manim import *
from equation import *

#class FunnelScene(Scene):
#    def construct(self):
#        cir = Circle()
#        sq = Square()
#
#        self.play(Create(sq))
#        self.play(Transform(sq, cir))
#        self.play(FadeOut(sq))

if __name__ == "__main__":
    equ = Function( lambda x,y: x**2 + y, 2 )
    equ_der = Function( lambda x,y: 2*x + 1, 2 )

    my_ode = ODE([equ, equ_der])

    points = []
    for i in range(0, 10):
        points.append(my_ode.get_point(i, -i))

    for point in points:
        print(f"{point}")

