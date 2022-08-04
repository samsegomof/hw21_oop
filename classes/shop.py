from .storage import Storage
from .exceptions import WarehouseFull


class Shop(Storage):
    """
    Может хранить до 5 наименований и в пределах емкости.
    """
    def __init__(self):
        super().__init__()
        self._capacity = 20

    def add(self, title: str, quantity: int) -> None:
        if self._get_unique_items_count() >= 5:
            raise WarehouseFull('В магазине нельзя хранить более 5ти наименований товаров')
        super().add(title, quantity)
