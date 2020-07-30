import pygame


class path_grid:
    def __init__(self, rect, kind):
        self.path_rect = rect
        self.kind = kind
        self.visited = False

    def getRect(self):
        return self.path_rect
