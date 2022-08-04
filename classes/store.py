from .storage import Storage


class Store(Storage):
    """
    Наследуется от склада - может хранить любое количество предметов и любые названия в пределах
    места на складе
    """

    def __init__(self):
        super().__init__()
        self._capacity = 100
