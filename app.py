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
    equ = Function( "x**2 + y", ["x", "y"] )
    equ_der = Function( "2*x + 1", ["x", "y"] )

    my_ode = ODE([equ, equ_der])

    points = []
    for i in range(0, 10):
        points.append(my_ode.get_point({"x": i, "y": -i}))

    for point in points:
        print(f"{point}")

