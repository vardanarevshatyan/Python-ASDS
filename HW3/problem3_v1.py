"""
## Problem 3
Use singleton pattern and classes of your choice. Create a structure where you have some resource that has states busy
and free and 3 users that try to use the resource and change the state to busy while they are using it. The resource
should be singleton. Implement using 2 different methods for singleton implementation that we have discussed.
"""
from time import sleep


class LoggerBorg:
    __state = dict()

    def __init__(self):
        self.__dict__ = self.__state  # stores class attributes
        self.state = 'free'
        self.user = None

    @staticmethod
    def log():
        print('Logging information, please wait...')
        sleep(.5)
        print('Done.')

    def connect(self, name):
        if self.state == 'free':
            self.state = 'busy'
            self.user = name
            print(f'User {self.user} connected to the LoggerBorg.')
        else:
            print(f'{name} unable to connect. Logger is busy. Try later.')

    def release(self):
        self.state = 'free'
        user = self.user
        self.user = None
        print(f'User {user} released the Borg.')


class User:
    def __init__(self, username):
        self.name = username
        self.logger = None

    def log(self):
        self.logger.log()

    def get_logger(self, logger):
        self.logger = logger
        self.logger.connect(self.name)

    def release_logger(self):
        if self.logger is not None:
            self.logger.release()
            self.logger = None


if __name__ == '__main__':
    borg = LoggerBorg()

    user1 = User('ImportantUser')
    user2 = User('KittyCat')
    user3 = User('Anonymous')

    user1.get_logger(borg)
    user1.log()
    user2.get_logger(borg)
    user3.get_logger(borg)
    user1.release_logger()
    user2.get_logger(borg)
    user2.log()
    user2.release_logger()