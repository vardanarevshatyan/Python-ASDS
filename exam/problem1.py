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


class DSHandler(AbstractHandler):
    keywords = ["analyze", "research", "model"]

    def handle(self, request: str) -> None:
        if any(keyword in request for keyword in self.keywords):
            print("DSHanlder handling task: ", request)
        else:
            return super().handle(request)


class DesignHandler(AbstractHandler):
    keywords = ["color", "decoration"]

    def handle(self, request: str) -> None:
        if any(keyword in request for keyword in self.keywords):
            print("DesignHandler handling task: ", request)
        else:
            return super().handle(request)


class QAHandler(AbstractHandler):
    keywords = ["test"]

    def handle(self, request: str) -> None:
        if any(keyword in request for keyword in self.keywords):
            print("QAHandler handling task: ", request)
        else:
            return super().handle(request)


class DefaultHandler(AbstractHandler):
    def handle(self, request: str) -> None:
        print("DefaultHandler handling task: ", request)


def handle_project_tasks(project_tasks: list) -> None:
    ds_handler = DSHandler()
    design_handler = DesignHandler()
    qa_handler = QAHandler()
    default_handler = DefaultHandler()
    ds_handler.set_successor(design_handler).set_successor(qa_handler).set_successor(default_handler)
    for task in project_tasks:
        ds_handler.handle(task)


if __name__ == "__main__":
    project = [
        "a model to separate the background",
        "test the application",
        "analyze the model",
        "choose the right color",
        "a model to separate the background",
        "test the input",
        "dicsuss the app decoration",
        "have a lunch with management",
    ]

    handle_project_tasks(project)
