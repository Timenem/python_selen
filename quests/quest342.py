"""
You often work with the different geometrical figures and with their parameters - the perimeter, area, and volume. You are tired of doing it manually, so you’ve decided to automate this process, and therefore you need to write a particular program. In this program you should create the class Parameters which will choose one of the few figures (the circle, regular triangle, square, regular pentagon, regular...
Also you have to create a class for each figure and use the
Every figure, except the cube, has the volume = 0.
If the result has no decimal places, you should return it as int(), in other case - round it to the 2 decimal points. 
"""

from abc import ABC, abstractmethod
from math import pi, sqrt

class Parameters:

    def __init__(self, a):
        self.a = a

    def choose_figure(self, shape):
        self.shape = shape
        
    def perimeter(self):
        return round(self.shape.perimeter(self.a), 2)

    def area(self):
        return round(self.shape.area(self.a), 2)

    def volume(self):
        return round(self.shape.volume(self.a), 2)

    
class Shape(ABC):

    @abstractmethod
    def area(self, a):
        pass

    @abstractmethod
    def perimeter(self, a):
        pass

    def volume(self, a):
        return 0


class Circle(Shape):

    def area(self, a):
        return a ** 2 * pi

    def perimeter(self, a):
        return 2 * pi * a
    

class Triangle(Shape):

    def area(self, a):
        return sqrt(3) / 4 * a ** 2

    def perimeter(self, a):
        return 3 * a


class Square(Shape):
    
    def area(self, a):
        return a ** 2

    def perimeter(self, a):
        return 4 * a


class Pentagon(Shape):
        
    def area(self, a):
        return sqrt(25 + 10 * sqrt(5)) / 4 * a ** 2

    def perimeter(self, a):
        return 5 * a


class Hexagon(Shape):
       
    def area(self, a):
        return (sqrt(3) * 3) / 2 * a ** 2

    def perimeter(self, a):
        return 6 * a


class Cube(Shape):
    
    def area(self, a):
        return 6 * a ** 2

    def perimeter(self, a):
        return 12 * a

    def volume(self, a):
        return a ** 3
