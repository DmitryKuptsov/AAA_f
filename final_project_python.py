from random import randint
from typing import Callable, Union, Any


class Margherita():
    def __init__(self, size: str = "L"):
        self.size = size

    def __eq__(self, other: Any) -> Any:
        """
        Функция проверяет экземпляры пиццы на равенство,
        равными они считаются только в том случае, если
        совпадает тип и размер.
        """
        return self.size == other.size and self.__class__ == other.__class__

    def dict(self) -> Union[dict[str, int], dict[str, str]]:
        """
        Выводит рецепт пиццы в виде словаря.
        """
        if self.size == "L":
            return {"tomato sauce": 1,
                    "mozzarella": 2,
                    "tomatoes": 5}
        elif self.size == "XL":
            return {"tomato sauce": 2,
                    "mozzarella": 3,
                    "tomatoes": 10}
        else:
            return {"Задан неправильный размер.": self.size}


class Pepperoni():
    def __init__(self, size: str = "L"):
        self.size = size

    def __eq__(self, other: Any) -> Any:
        """
        Функция проверяет экземпляры пиццы на равенство,
        равными они считаются только в том случае, если
        совпадает тип и размер.
        """
        return self.size == other.size and self.__class__ == other.__class__

    def dict(self) -> Union[dict[str, int], dict[str, str]]:
        """
        Выводит рецепт пиццы в виде словаря.
        """
        if self.size == "L":
            return {"tomato sauce": 1,
                    "mozzarella": 2,
                    "pepperoni": 8}
        elif self.size == "XL":
            return {"tomato sauce": 2,
                    "mozzarella": 3,
                    "pepperoni": 12}
        else:
            return {"Задан неправильный размер.": self.size}


class Hawaiian():
    def __init__(self, size: str = "L"):
        self.size = size

    def __eq__(self, other: Any) -> Any:
        """
        Функция проверяет экземпляры пиццы на равенство,
        равными они считаются только в том случае, если
        совпадает тип и размер.
        """
        return self.size == other.size and self.__class__ == other.__class__

    def dict(self) -> Union[dict[str, int], dict[str, str]]:
        """
        Выводит рецепт пиццы в виде словаря.
        """
        if self.size == "L":
            return {"tomato sauce": 1,
                    "mozzarella": 2,
                    "chicken": 1,
                    "pineapples": 1}
        elif self.size == "XL":
            return {"tomato sauce": 2,
                    "mozzarella": 3,
                    "chicken": 2,
                    "pineapples": 2}
        else:
            return {"Задан неправильный размер.": self.size}


def log(param: str) -> Callable[[Callable[[Any], Any]], Callable[[], Any]]:
    """
    Декоратор с параметрами, на вход получает строку,
    вставляет в нее время выполнения задачи.
    """
    def outer_wrapper(func: Callable[[Any], Any]) -> Callable[[], Any]:
        def inner_wrapper(*args: Any, **kwargs: Any) -> Any:
            print(param.replace("{}", str(randint(1, 5))))
            return func(*args, **kwargs)
        return inner_wrapper
    return outer_wrapper


@log(" Доставили за {}с!")
def delivery(pizza: Any) -> Any:
    """Доставляет пиццу"""
    return pizza


@log(" Забрали за {}с!")
def pickup(pizza: Any) -> Any:
    """Самовывоз"""
    return pizza


@log(" Приготовили за {}с!")
def bake(pizza: Any) -> Any:
    """Готовит пиццу"""
    return pizza


if __name__ == "__main__":
    pass
