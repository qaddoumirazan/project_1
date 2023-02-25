from inhiretance.circle import Circle
from math import pi

class Cylinder(Circle):
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
    def volume(self):
        vol = (3/4)* pi *self.radius**3
        return vol