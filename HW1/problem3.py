from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def draw(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def draw(self):
        pass


class WinButton(Button):
    def draw(self):
        print('I draw Windows Button.')


class MacButton(Button):
    def draw(self):
        print('I draw Mac Button.')


class WinCheckbox(Checkbox):
    def draw(self):
        print('Windows checked.')


class MacCheckbox(Checkbox):
    def draw(self):
        print('Mac checked.')


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.checkbox = self.factory.create_checkbox()
        self.button = self.factory.create_button()

    def paint(self):
        self.checkbox.draw()
        self.button.draw()


if __name__ == '__main__':
    factory = MacFactory()
    app = Application(factory)
    app.create_ui()
    app.paint()