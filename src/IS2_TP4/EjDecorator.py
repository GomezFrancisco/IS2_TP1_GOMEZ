class Number:
    """
    The base Number class defines the interface for interacting with a number.
    """

    def __init__(self, value: int) -> None:
        self._value = value

    def operation(self) -> int:
        return self._value


class NumberDecorator(Number):
    """
    The base NumberDecorator class follows the same interface as the Number class.
    It delegates all work to the wrapped Number instance.
    """

    def __init__(self, number: Number) -> None:
        self._number = number

    def operation(self) -> int:
        return self._number.operation()


class AddTwoDecorator(NumberDecorator):
    """
    The AddTwoDecorator adds 2 to the number.
    """

    def operation(self) -> int:
        return self._number.operation() + 2


class MultiplyByTwoDecorator(NumberDecorator):
    """
    The MultiplyByTwoDecorator multiplies the number by 2.
    """

    def operation(self) -> int:
        return self._number.operation() * 2


class DivideByThreeDecorator(NumberDecorator):
    """
    The DivideByThreeDecorator divides the number by 3.
    """

    def operation(self) -> int:
        return self._number.operation() // 3


if __name__ == "__main__":
    # Creating a simple number
    number = Number(5)
    print("Simple Number:")
    print(f"RESULT: {number.operation()}")
    print("\n")

    # Adding decorators one by one
    decorated_number = AddTwoDecorator(number)
    print("Number with AddTwoDecorator:")
    print(f"RESULT: {decorated_number.operation()}")
    
    decorated_number = MultiplyByTwoDecorator(decorated_number)
    print("Number with MultiplyByTwoDecorator:")
    print(f"RESULT: {decorated_number.operation()}")
    
    decorated_number = DivideByThreeDecorator(decorated_number)
    print("Number with DivideByThreeDecorator:")
    print(f"RESULT: {decorated_number.operation()}")
