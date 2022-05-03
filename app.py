#!/usr/bin/python

from manim import *
from equation import Equation

class FunnelScene(Scene):
    def construct(self):
        cir = Circle()
        sq = Square()

        self.play(Create(sq))
        self.play(Transform(sq, cir))
        self.play(FadeOut(sq))
