from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def __init__(self):
        self.name = None
        self.color = None

