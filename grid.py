import pygame


class path_grid:
    path_rect = None
    def __init__(self, rect, kind):
        self.path_rect = rect
        self.kind = kind