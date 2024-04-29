from __future__ import annotations
from abc import ABC, abstractmethod
from random import choice
from typing import List

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    _state: str = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print(f"Subject: Attached an observer with ID {observer.id}.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def emit_id(self, id: str) -> None:
        self._state = id
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    def __init__(self, id: str):
        self.id = id

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class ConcreteObserver(Observer):
    def update(self, subject: Subject) -> None:
        if self.id == subject._state:
            print(f"Observer {self.id}: Reacted to the event")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer1 = ConcreteObserver("ID01")
    subject.attach(observer1)

    observer2 = ConcreteObserver("ID02")
    subject.attach(observer2)

    observer3 = ConcreteObserver("ID03")
    subject.attach(observer3)

    observer4 = ConcreteObserver("ID04")
    subject.attach(observer4)

    ids = ["ID01", "ID02", "ID03", "ID04", "ID05", "ID06", "ID07", "ID08"]
    for _ in range(8):
        subject.emit_id(choice(ids))
