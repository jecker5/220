"""
Name: Joseph Decker
sphere.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


class Sphere:
    """ Creating a Sphere """
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return float(self.radius)

    def surface_area(self):
        surface_area = 4 * math.pi * (self.radius**2)
        return float(surface_area)

    def volume(self):
        volume = (4/3) * math.pi * (self.radius**3)
        return volume
