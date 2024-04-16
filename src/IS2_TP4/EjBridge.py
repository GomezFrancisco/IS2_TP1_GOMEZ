from __future__ import annotations
from abc import ABC, abstractmethod


class Laminator(ABC):
    """
    The Implementation defines the interface for all concrete laminator
    classes.
    """

    @abstractmethod
    def produce_sheet(self, width: float) -> str:
        pass


class FiveMeterLaminator(Laminator):
    def produce_sheet(self, width: float) -> str:
        return f"Producing sheet of {width} meters using the 5-meter laminator."


class TenMeterLaminator(Laminator):
    def produce_sheet(self, width: float) -> str:
        return f"Producing sheet of {width} meters using the 10-meter laminator."


class SteelSheet:
    """
    The Abstraction defines the interface for the "control" part of the
    hierarchy.
    """

    def __init__(self, thickness: float, width: float, laminator: Laminator) -> None:
        self.thickness = thickness
        self.width = width
        self.laminator = laminator

    def produce(self) -> str:
        return f"Steel sheet of {self.thickness} inches and {self.width} meters wide. {self.laminator.produce_sheet(self.width)}"


if __name__ == "__main__":
    # Using a 5-meter laminator
    steel_sheet_5m = SteelSheet(0.5, 1.5, FiveMeterLaminator())
    print(steel_sheet_5m.produce())

    # Using a 10-meter laminator
    steel_sheet_10m = SteelSheet(0.5, 1.5, TenMeterLaminator())
    print(steel_sheet_10m.produce())
