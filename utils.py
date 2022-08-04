from sys import exit
from typing import Tuple, List

from classes import ItemsNotFound, MessageError, WarehouseFull
from classes import Store, Shop, Request


def create_instances(items_shop: List[Tuple[str, int]], items_store: List[Tuple[str, int]]) -> [Shop, Store]:
    shop = Shop()
    for item in items_shop:
        shop.add(*item)

    store = Store()
    for item in items_store:
        store.add(*item)

    return shop, store


def displays_items(shop: Shop, store: Store) -> str:
    header_store = 'В склад хранится:\n'
    header_shop = '\nВ магазин хранится:\n'
    return (header_store
            + '\n'.join([f'{value} {key}' for key, value in store.get_items().items()])
            + '\n'
            + header_shop
            + '\n'.join([f'{value} {key}' for key, value in shop.get_items().items()]))


def send_request(user_task: str, shop: Shop, store: Store) -> str:
    if user_task.lower() == 'стоп':
        exit()
    try:
        request = Request({'магазин': shop, 'склад': store}, user_task)
        request.process()
        return (f'\nВаш запрос принят, товар в нужном количестве есть в наличии\n'
                f'Курьер доставил {request.amount} {request.product} из {request.from_} в {request.to}\n')
    except (MessageError, WarehouseFull, ItemsNotFound) as e:
        print(e)
        user_task = input('Попробуйте еще раз: ')
        send_request(user_task, shop, store)
