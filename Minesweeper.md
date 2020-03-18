import random

class Cell(object):
    def __init__(self, is_mine, is_visible=False, is_flagged=False):
        self.is_mine = is_mine
        self.is_visible = is_visible
        self.is_flagged = is_flagged

    def show(self):
        self.is_visible = True
