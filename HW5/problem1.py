class Person:
    def __init__(self, name, surname, email, age):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age

    def print_information(self):
        info = self.get_information()
        print(*info, sep=' - ')

    def get_information(self):
        info = [self.name, self.surname, self.email]
        return info


class PersonDecorator:
    def __init__(self, person):
        self._person = person

    @property
    def person(self):
        return self._person

    def print_information(self):
        info = self.get_information()
        print(*info, sep=' - ')

    def get_information(self):
        info = self._person.get_information()
        if self._person.age < 14:
            pattern = '*** &&&'
        else:
            pattern = '&&&'
        info[0] = pattern + ' ' + info[0]
        info[-1] = info[-1] + ' ' + pattern
        return info


if __name__ == '__main__':
    john = Person('John', 'Smith', 'sjohn@yahoo.com', 27)
    sarah = Person('Sarah', 'Lynn', 'slynn@gmail.com', 12)
    john = PersonDecorator(john)
    sarah = PersonDecorator(sarah)
    john.print_information()
    sarah.print_information()
