"""
## Problem 1
Suppose that you have some images that need to be loaded from some server and be shown to
the user. Since the loading may take some time, we want to have proxy images in case the real
images are not loaded after some fixed amount of time. Simulate this scenario with classes of
your choice and using proxy design pattern principle
"""

import signal
from abc import ABC, abstractmethod
from time import sleep, time

from numpy import random


class ImageService(ABC):
    @abstractmethod
    def load_image(self):
        pass


class ImageLoader(ImageService):
    def load_image(self):
        # simulating the loading time...
        rand_time = random.randint(1, 4)
        print("Loading the image...")
        sleep(rand_time)
        print("Image loaded successfully...")


class TimeOutException(Exception):
    pass


# this will not work on windows ;(
class ImageLoaderProxy(ImageService):
    def __init__(self, loader: ImageService):
        self._service = loader

    def handle_time(self, signum, frame):
        raise TimeOutException

    def load_image(self):
        signal.signal(signal.SIGALRM, self.handle_time)
        signal.alarm(2)
        try:
            self._service.load_image()
        except TimeOutException:
            print("Loading took too long!")
            print("Proxy image is printed.")


if __name__ == "__main__":
    proxy = ImageLoaderProxy(ImageLoader())
    # simulating different loading times
    for _ in range(5):
        proxy.load_image()
