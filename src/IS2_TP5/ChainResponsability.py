from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class EvenHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request % 2 == 0:
            return f"El número {request} es par."
        else:
            return f"El número {request} es impar."


class PrimeHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request > 1:
            for i in range(2, request):
                if (request % i) == 0:
                    break
            else:
                return f"El número {request} es primo."
        return super().handle(request)


def client_code(handler: Handler) -> None:
    for number in range(1, 101):
        result = handler.handle(number)
        if result:
            print(result, end="\n")


if __name__ == "__main__":
    even = EvenHandler()
    prime = PrimeHandler()

    even.set_next(prime)

    print("Cadena: Par > Primo\n")
    client_code(even)
    print("\n")
