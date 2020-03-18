""" Ezekiel M. Bustillo
    DATALOGO Lab04
    Feb. 19, 2020
    I have neither received nor provided any help on this (lab) activity,
    nor have I concealed any violation of the Honor Code.
"""
from abc import ABCMeta, abstractmethod

class Polygon(metaclass=ABCMeta):
    def __init__(self, lengths):
        self.no_sides = len(lengths)
        self.lengths = [0] * self.no_sides
        self.val(lengths)
    def numsides(self):
        print('The polygon has ' + str(self.no_sides) + 'sides.')
    def val(self, lengths):
        a = 0
        while a < len(lengths):
            self.lengths[a] = lengths[a]
            a += 1
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Pentagon(Polygon):
    def __init__(self, lengths):
        super().__init__(lengths)
        assert 5, self.no_sides
    def area    (self):
        x, y = self.lengths[0], self.lengths[1]
        return x * y
    def perimeter(self):
        x, y = self.lengths
        return (x+y)*2

class Hexagon(Polygon):
    def __init__(self, lengths):
        super().__init__(lengths)
        assert 6, self.no_sides
    def area(self):
        x, y = self.lengths[0], self.lengths[1]
        return x * y
    def perimeter(self):
        x, y = self.lengths
        return (x+y)*2

if __name__=="__main__":
