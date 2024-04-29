from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    def __init__(self, collection: str = '') -> None:
        self._collection = list(collection)

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)


if __name__ == "__main__":
    cadena = input("Por favor, ingresa una cadena de caracteres: ")
    collection = WordsCollection(cadena)
    print("Recorrido directo:")
    print("".join(collection))
    print("")

    print("Recorrido inverso:")
    print("".join(collection.get_reverse_iterator()), end="")
    print("\n")
