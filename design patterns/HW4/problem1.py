"""
## Problem 1
Let say you want to send a message to someone. You have 2 options - you can Email the message or SMS the message to the
corresponding person. So, you have two options to send the message and the client side code will use one of the
implementations to send the message to the corresponding person. Use Bridge Design Pattern to implement the logic with
classes of your choice and make sure to test the implementation with some concrete objects.
"""
from abc import ABC, abstractmethod
from time import sleep


class Messenger:
    def __init__(self, implementation) -> None:
        self._implementation = implementation

    def send_message(self, contact, text):
        self.set_contact(contact)
        self._implementation.send_message(text)

    def set_contact(self, contact):
        self._implementation.contact = contact

    def get_contact(self):
        return self._implementation.contact


class Sender(ABC):
    @abstractmethod
    def send_message(self, text):
        pass

    @property
    @abstractmethod
    def contact(self):
        pass

    @contact.setter
    @abstractmethod
    def contact(self, val):
        pass


class EmailSender(Sender):
    def __init__(self):
        self._contact = None

    def send_message(self, text):
        print(f"Sending to {self._contact}...")
        sleep(0.7)
        print(f"Sent: {text}")

    @property
    def contact(self):
        if self._contact is None:
            print("You have not chosen a contact.")
            return
        print(f"Retrieving the email address: {self._contact}")
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value


class SMSSender(Sender):
    def __init__(self):
        self._contact = None

    def send_message(self, text):
        print(f"Sending to {self._contact}...")
        sleep(0.7)
        print(f"Sent: {text}")

    @property
    def contact(self):
        if self._contact is None:
            print("You have not chosen a phone number.")
            return
        print(f"Retrieving the phone number: {self._contact}")
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value


class Client:
    senders = {"email": Messenger(EmailSender()), "sms": Messenger(SMSSender())}

    @classmethod
    def send_message(cls, by, contact, text):
        messenger = cls.senders.get(by, None)
        if messenger is None:
            print("Please choose a valid option.")
            return
        messenger.send_message(contact, text)


if __name__ == "__main__":
    client = Client()
    client.send_message(
        "email", "someone@gmail.com", "Hey, I have a great job opportunity for you!"
    )
    client.senders["email"].get_contact()
    client.send_message("sms", "+209145909", "Hey Sam, how are u?")
    client.senders["sms"].get_contact()
    client.send_message("facebook", "fb_id", "Hiii!")
