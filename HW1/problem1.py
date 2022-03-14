"""
## Problem 1
Use Factory Method pattern to create 3 different classes Circle, Square and Triangle of type
Shape having a method Draw with some implementation of your choice. Have a ShapeFactory
class and a Client class and allow the Client to ask the factory to create some concrete shape
and to call its method Draw. You can decide what should be the client input and how the factory
class should determine which shape to create.
"""

from abc import ABC, abstractmethod
import turtle
from math import pi, sqrt


class Shape(ABC):
    """Base class providing product interface."""
    @abstractmethod
    def __init__(self, length):
        self._length = length

    """Simple implementations with Turtle."""
    @abstractmethod
    def draw(self, *args, **kwargs):
        pass

    """Calculate the area of the geometric shape. Defined as property. It is here to add some variability to 
    implementation. """
    @property
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, length):
        super().__init__(length)

    def draw(self):
        t = turtle.Turtle()
        t.circle(self._length)

    @property
    def area(self):
        return pi * self._length**2


class Triangle(Shape):
    def __init__(self, length):
        super().__init__(length)

    def draw(self):
        t = turtle.Turtle()
        for i in range(3):
            t.forward(self._length)
            t.left(120)

    @property
    def area(self):
        return self._length ** 2 * sqrt(3) / 4


class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def draw(self):
        t = turtle.Turtle()
        for i in range(4):
            t.forward(self._length)
            t.left(90)

    @property
    def area(self):
        return self._length ** 2


class ShapeFactory:
    SHAPES = {
        'circle': Circle,
        'square': Square,
        'triangle': Triangle,
    }

    @classmethod
    def build(cls, shape_name: str, length: int):
        return cls.SHAPES[shape_name](length)


class Client:

    @staticmethod
    def draw_shape(shape_name: str, length: int):
        shape = ShapeFactory.build(shape_name, length)
        shape.draw()

    @staticmethod
    def get_shape_area(shape_name: str, length: int):
        # this is a little repetitive, but it's fine for the problem
        shape = ShapeFactory.build(shape_name, length)
        return shape.area


if __name__ == '__main__':
    client = Client()
    client.draw_shape('square', 100)
    client.draw_shape('circle', 50)
    client.draw_shape('triangle', 150)
    print(client.get_shape_area('square', 100))
