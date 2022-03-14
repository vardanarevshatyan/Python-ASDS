"""
## Problem 2
Follow the diagram below and use Composite Design Pattern to implement and test the logic. Add any other classes of your
choice. The top of your hierarchy will be the box which will contain Instrument Collection which will contain
instruments.
"""
from abc import ABC, abstractmethod


class Instrument(ABC):
    @abstractmethod
    def make(self):
        pass


class Pen(Instrument):
    def __init__(self, name, price_tag):
        self.name = name
        self.price_tag = price_tag

    def make(self):
        print(f'{self.price_tag} {self.name} to write.')


class Pencil(Instrument):
    def __init__(self, name, price_tag):
        self.name = name
        self.price_tag = price_tag

    def make(self):
        print(f'{self.price_tag} {self.name} to draw.')


class Rubber(Instrument):
    def __init__(self, name, price_tag):
        self.name = name
        self.price_tag = price_tag

    def make(self):
        print(f'{self.price_tag} {self.name} to erase.')


class Box(Instrument):
    def __init__(self, name, price_tag):
        self.name = name
        self.price_tag = price_tag
        self._instruments = []

    def add(self, instrument):
        self._instruments.append(instrument)

    def remove(self, instrument):

        self._instruments.remove(instrument)

    def get_child(self, index):
        return self._instruments[index]

    def make(self):
        print(f'{self.price_tag} {self.name} box is used, containing: ')
        for instrument in self._instruments:
            print('\t', end="")
            instrument.make()


if __name__ == '__main__':
    box1 = Box(name='FancyBox', price_tag='Expensive')
    box2 = Box(name='OkayBox', price_tag='Average Quality')
    pen1 = Pen(name='FancyBlackPen', price_tag='Very Expensive')
    pen2 = Pen(name='AveragePen', price_tag='Pretty Cheap')
    pencil1 = Pencil(name='LuxuriousPencil', price_tag='Super Expensive')
    pencil2 = Pencil(name='ModeratePencil', price_tag='DecentQuality')
    rubber1 = Rubber(name='SolidRubber', price_tag='Decent Quality')
    rubber2 = Rubber(name='CouldBeBetterRubber', price_tag='Super Cheap')

    box1.add(pen1)
    box1.add(pencil1)
    box1.add(rubber1)
    box1.make()
    print('\n')
    box2.add(pen2)
    box2.add(pencil2)
    box2.add(rubber2)
    box2.make()


