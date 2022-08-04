from typing import Tuple, Any

from .exceptions import MessageError


class Request:

    def __init__(self, storages: dict, message: str):
        self._storages = storages
        self._message = message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value: str) -> None:
        Request._split_message(value)
        self._message = value

    @property
    def from_(self) -> str:
        return Request._split_message(self.message)['from']

    @property
    def to(self) -> str:
        return Request._split_message(self.message)['to']

    @property
    def product(self) -> str:
        return Request._split_message(self.message)['product']

    @property
    def amount(self) -> int:
        return int(Request._split_message(self.message)['amount'])

    @staticmethod
    def _split_message(message: str) -> dict:
        message = message.split(' ')

        if len(message) < 7:
            raise MessageError('Сообщение некорректное')

        split_message = {'from': message[4], 'to': message[6], 'amount': message[1], 'product': message[2]}

        if (
            split_message['from'] not in ['склад', 'магазин']
            or split_message['to'] not in ['склад', 'магазин']
            or not split_message['amount'].isdigit()
        ):
            raise MessageError('Сообщение некорректное')

        return split_message

    def process(self) -> Tuple[Any, Any]:
        self._storages[self.from_].remove(self.product, self.amount)
        self._storages[self.to].add(self.product, self.amount)
        return self._storages[self.from_], self._storages[self.to]

    def __repr__(self):
        return f'from: {self.from_}, to: {self.to}, amount: {self.amount}, product: {self.product}'











