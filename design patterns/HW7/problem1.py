"""
## Problem 1
Imagine that you have the following scenario: you have a file containing some text, in case the text contains the word "error",
you want to log it as an error using the ErrorLogger, otherwise, if the text contains the word "file", you should log
something in a new file using the FileLogger, otherwise, if its not one of the 2 cases, you need to log something in the console,
using the ConsoleLogger. Feel free to simulate the work of the loggers however you wish, you don't even have to actually write something in
the file, just differentiate the 3 operations in some way. The actions of logging can be simple print statements, they just need to be different
for error logs, console logs and file logs. You need to implement this logic using chain of responsibility design pattern and classes of your choice.
You may (or may not) use the diagram below as a guide.
"""
from __future__ import annotations

from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def handle(self, request: str) -> None:
        pass

    @abstractmethod
    def set_successor(self, successor: Handler) -> None:
        pass


class AbstractHandler(Handler):
    _successor = None

    def set_successor(self, successor: Handler) -> None:
        self._successor = successor
        return successor

    def handle(self, request: str) -> None:
        if self._successor:
            return self._successor.handle(request)
        return None


class ErrorLogger(AbstractHandler):
    def handle(self, request: str) -> None:
        if "error" in request:
            print("Error Logged")
        else:
            return super().handle(request)


class FileLogger(AbstractHandler):
    def handle(self, request: str) -> None:
        if "file" in request:
            print("File Logged")
        else:
            return super().handle(request)


class ConsoleLogger(AbstractHandler):
    def handle(self, request: str) -> None:
        print("Neither error nor file.", request)


def client_code(handler: Handler) -> None:
    for log in ["There is a file error in this request!", "Need to log the file.", "Cup of coffee"]:
        result = handler.handle(log)
        if result:
            print(f"{result}", end="")


if __name__ == "__main__":
    err = ErrorLogger()
    fl = FileLogger()
    cns = ConsoleLogger()
    err.set_successor(fl).set_successor(cns)
    client_code(err)
