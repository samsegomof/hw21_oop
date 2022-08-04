class WarehouseFull(Exception):
    """
    Вызывается, когда нет свободного места на складе
    """
    def __init__(self, message='Not enough capacity!'):
        self.message = message
        super().__init__(message)


class ItemsNotFound(Exception):
    """
    Вызывается когда передано не сохраненное название или количество превышает сохраненное
    """
    def __init__(self, message='Items not found!'):
        self.message = message
        super().__init__(message)


class MessageError(Exception):
    """
    Если передано неправильное сообщение
    """
    def __init__(self, message='Incorrect message'):
        self.message = message
        super().__init__(message)






























