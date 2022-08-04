from abc import ABC, abstractmethod

from .exceptions import WarehouseFull, ItemsNotFound


class Storage(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def __init__(self):
        self._items: {str: int} = {}
        self._capacity = 0

    def __repr__(self):
        return f'Это склад типа {self.__class__.__name__} с вместимостью {self._capacity}'

    def add(self, title: str, quantity: int) -> None:
        """Добавляет предмет на склад

        :raises WarehouseFull: Если нет места на складе.
        """
        if self._get_free_space() < quantity:
            raise WarehouseFull('Склад заполнен, места нет!')
        self._items[title] = self._items.get(title, 0) + quantity

    def remove(self, title: str, quantity: int) -> None:
        """
        Удаляет количество предметов со склада

        :raises ItemsNotFound: Если нет предмета с указанным наименованием на складе.
        :raises ItemsNotFound: Если нет нужного количества предметов с указанным наименованием.
        """
        if title not in self._items.keys():
            raise ItemsNotFound(f'Нет товара с наименованием {title}')
        if quantity > self._items.get(title):
            raise ItemsNotFound(f'Нет нужного количества товара с наименованием {title}')

        self._items[title] = self._items.get(title) - quantity
        if self._items[title] == 0:
            del self._items[title]

    def _get_free_space(self) -> int:
        """
        Получаем свободное место на складе
        """
        using_space = sum([item for item in self._items.values()])
        return self._capacity - using_space

    def get_items(self) -> dict:
        """
        :return: словарь с сохраненными предметами
        """
        return self._items

    def _get_unique_items_count(self) -> int:
        """
        :return: количество уникальных предметов на складе
        """
        return len([item for item in self._items.keys()])
