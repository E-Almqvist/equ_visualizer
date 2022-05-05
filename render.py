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
    
class Point_2D:
    def __init__(self, parent, x, y, col=(255, 255, 255)):
        self.parent = parent
        self.x = x
        self.y = y
        self.col = col

    def coord(self, scale=1, offset_x=0, offset_y=0):
        x_coord = int( scale*(self.x + offset_x) )
        y_coord = int( scale*(self.y + offset_y) )
        return (x_coord, y_coord)

    def render(self, window, scale=1):
        x, y = self.coord(scale, 0, 0)
        x = int(window.w/2 - x/2)
        y = int(window.h/2 - y/2)
        window.window.set_at((x,y), self.col)

class RenderSpace(Window):
    def __init__(self, points=[], **kwargs):
        super().__init__(**kwargs)
        self.points = points

    def render(self, scale=1):
        pygame.init()
        self.window = pygame.display.set_mode( (self.w, self.h) )

        self.run = True
        while self.run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False

            self.window.fill(0)
            # X AXIS
            pygame.draw.line(self.window, (180, 180, 180), (0, self.h/2), (self.w, self.h/2), 1)
            # Y AXIS
            pygame.draw.line(self.window, (180, 180, 180), (self.w/2, 0), (self.w/2, self.h), 1)

            for p in self.points:
                p.render(self, scale)
            pygame.display.flip()


