from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class Leaf(Component):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.
    """

    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
    The Composite class represents the complex components that may have
    children.
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


class SubAssembly(Composite):
    """
    SubAssembly class represents a subset of components within the main assembly.
    """

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"SubAssembly({'+'.join(results)})"


class OptionalSubAssembly(SubAssembly):
    """
    OptionalSubAssembly class represents an optional subset of components within the main assembly.
    """

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"OptionalSubAssembly({'+'.join(results)})"


if __name__ == "__main__":

    print("\n")

    # Main assembly with three sub-assemblies
    main_assembly = Composite()

    sub_assembly1 = SubAssembly()
    for _ in range(4):
        sub_assembly1.add(Leaf())

    sub_assembly2 = SubAssembly()
    for _ in range(4):
        sub_assembly2.add(Leaf())

    sub_assembly3 = SubAssembly()
    for _ in range(4):
        sub_assembly3.add(Leaf())

    main_assembly.add(sub_assembly1)
    main_assembly.add(sub_assembly2)
    main_assembly.add(sub_assembly3)

    # Display main assembly
    print("Main Assembly:")
    print(main_assembly.operation())
    print("\n")

    # Adding an optional sub-assembly
    optional_sub_assembly = OptionalSubAssembly()
    for _ in range(4):
        optional_sub_assembly.add(Leaf())

    main_assembly.add(optional_sub_assembly)

    # Display main assembly with optional sub-assembly
    print("Main Assembly with Optional Sub-Assembly:")
    print(main_assembly.operation())
