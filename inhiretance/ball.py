from math import pi

from inhiretance.circle import Circle


class Ball(Circle):
    def __init__(self,radius):
        self.radius = radius
    def vol(self):
        vol = (3/4)*pi * self.radius**3
        return vol
