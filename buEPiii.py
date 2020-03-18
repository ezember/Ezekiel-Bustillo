""" Ezekiel M. Bustillo
    DATALGO Lab05
    Feb. 26, 2020
    I have neither received nor provided any help on this (lab) activity,
    nor have I concealed any violation of the Honor Code.
"""


class Airplane:
    def __init__(self):
        self.speed=0
    def set_speed(self,speed):
        self.speed=speed
    def get_speed(self):
        return self.speed

class Jet(Airplane):
    def __init__(self):
        super().__init__()
        self.MULTIPLIER=2
    def set_speed(self,speed):
        super().set_speed (speed*self.MULTIPLIER)
    def accelerate(self):
        super().set_speed (self.get_speed()*2)

class FlyTest():
    biplane=Airplane()
    biplane.set_speed(212)
    print(biplane.set_speed)
    boeing=Jet()
    boeing.set_speed(422)
    print(boeing.set_speed)
    x=0
    while x >= 1:
        boeing.get_speed()
        print(boeing.get_speed)
        if boeing.get_speed () > 5000:
            boeing.get_speed() * (boeing.get_speed() *2)
        else:
            boeing.accelerate()
        boeing.set_speed(424)
    print(boeing.accelerate())


FlyTest()


