#from manim import *
#import math
import pygame

# class EquationScene(Scene):
#     def construct(self):
#         ax = Axes(x_range=[-100, 100, 50], y_range=[-100, 100, 50], x_length=10, y_length=10, axis_config={"include_tip": False})
#         self.add(ax)
#         self.wait(4)

class Window:
    def __init__(self, w: int=1600, h: int=900):
        self.w = w
        self.h = h
        self.run = False
    
    def open(self):
        pygame.init()
        self.window = pygame.display.set_mode( (self.w, self.h) )
        self.run = True
        while self.run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False
            self.window.fill(0)

class Point_2D:
    def __init__(self, parent_window, x, y, col=(255, 255, 255)):
        self.parent_window = parent_window
        self.x = x
        self.y = y
        self.col = col

    def render(self):
        parent_window.window.set_at((self.x, self.y), self.col)

class RenderSpace(Window):
    def __init__(self, points=[], **kwargs):
        super().__init__(**kwargs)
        self.points = points

    def render(self):
        super().open()
        for p in self.points:
            p.render()


