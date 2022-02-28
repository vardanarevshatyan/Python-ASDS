class ClassicLogger:
    __shared_instance = 'initial'

    @staticmethod
    def get_instance():
        """Static Access Method"""
        if ClassicLogger.__shared_instance == 'initial':
            ClassicLogger()
        if ClassicLogger.__shared_instance._state == 'free':
            ClassicLogger.__shared_instance._state = 'busy'
            return ClassicLogger.__shared_instance
        else:
            raise Exception('Logger is locked. Try later.')

    def __init__(self):
        self._state = 'free'
        if ClassicLogger.__shared_instance != 'initial':
            raise Exception("This class is a singleton class !")
        else:
            ClassicLogger.__shared_instance = self


class User:
    def __init__(self, username):
        self.name = username
        self.logger = None

    def get_logger(self):
        try:
            self.logger = ClassicLogger.get_instance()
            print(f'{self.name} established a connection.')

        except BaseException as e:
            print(e)

    def release_logger(self):
        if self.logger is not None:
            print(f'{self.name} released the connection.')
            self.logger._state = 'free'
            self.logger = None


if __name__ == '__main__':
    user1 = User('ImportantUser')
    user2 = User('KittyCat')
    user3 = User('Anonymous')

    user1.get_logger()
    user2.get_logger()
    user3.get_logger()
    user1.release_logger()
    user2.get_logger()
    user2.release_logger()
    user3.get_logger()
    user3.release_logger()
