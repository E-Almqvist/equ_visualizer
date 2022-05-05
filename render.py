from manim import *
import math

class EquationScene(Scene):
    def construct(self):
        ax = Axes(x_range=[-100, 100, 50], y_range=[-100, 100, 50], x_length=10, y_length=10, axis_config={"include_tip": False})
        self.add(ax)
        self.wait(4)

