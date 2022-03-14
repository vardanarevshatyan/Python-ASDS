"""
## Problem 2
Use prototype design pattern and classes of your choice. create an abstract class Shape and
concrete classes extending the Shape class: Circle, Square and Rectangle. Define a class
ShapeCache which stores shape objects in a dictionary and returns their clones when
requested. Create some objects and do some operations to test your classes.
"""
from abc import ABC, abstractmethod
from copy import copy
from time import sleep, perf_counter


class Shape(ABC):
    @abstractmethod
    def __init__(self, name, color):
        self._name = name
        self.color = color

    @property
    @abstractmethod
    def name(self):
        return self._name

    @abstractmethod
    def draw(self, *args, **kwargs):
        pass

    """Calculate the area of the geometric shape. Defined as property. It is here to add some variability to 
    implementation. """

    def clone(self):
        return copy(self)


class Circle(Shape):
    def __init__(self, name=None, color=None):
        sleep(.5)
        super().__init__(name, color)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def draw(self):
        print(f'Draw {self.color} {self.name}')


class Square(Shape):
    def __init__(self, name=None, color=None):
        sleep(.5)
        super().__init__(name, color)

    def draw(self):
        print(f'Draw {self.color} {self.name}')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Rectangle(Shape):
    def __init__(self, name=None, color=None):
        sleep(.5)
        super().__init__(name, color)

    def draw(self):
        print(f'Draw {self.color} {self.name}')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class ShapeCache:
    cache = {}

    @classmethod
    def get_shape(cls, name):
        crs = cls.cache.get(name, None)
        return crs.clone()

    @classmethod
    def load(cls):
        start = perf_counter()
        circle = Circle(color='red')
        print('Circle loaded.')
        circle.name = 'funny_circle'
        rect = Rectangle(color='green')
        print('Rectangle loaded.')
        rect.name = 'boo_rectangle'
        square = Square(color='black')
        print('Square loaded.')
        square.name = 'spooky_square'
        end = perf_counter()
        print('Expensive load: ', end-start)
        cls.cache[circle.name] = circle
        cls.cache[rect.name] = rect
        cls.cache[square.name] = square


if __name__ == '__main__':
    #expensive load
    ShapeCache.load()
    start = perf_counter()
    circle = ShapeCache.get_shape('funny_circle')
    sqr = ShapeCache.get_shape('spooky_square')
    rect = ShapeCache.get_shape('boo_rectangle')
    end = perf_counter()
    print('From cache: ', end-start)