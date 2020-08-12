import sys

class path_grid:
    def __init__(self, rect, kind, pos):
        self.path_rect = rect
        self.kind = kind
        self.visited = False
        self.position = pos
        self.F_value = sys.float_info.max
        self.H_value = sys.float_info.max
        self.G_value = sys.float_info.max
        self.parentCol = -1
        self.parentRow = -1
    def getRect(self):
        return self.path_rect
