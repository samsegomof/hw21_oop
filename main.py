from sys import exit

from classes import items_shop, items_store
from utils import send_request, displays_items, create_instances


def main():
    print('Привет! Это симулятор логистических процессов между складом и магазином\n'
          '\nДля отправления товара нужно ввести сообщение\n'
          'Формат: Доставить [кол-во] [наименование] из [откуда] в [куда]\n'
          'Пример: Доставить 2 слон из склад в магазин\n'
          '\nДля остановки программы в любой момент введите "стоп"\n'
          'Для начала работы нажмите Enter')
    user_input = input()

    if user_input == 'стоп':
        exit()

    shop, store = create_instances(items_shop, items_store)

    while True:
        print(displays_items(store=store, shop=shop))

        user_task = input('\nВведите название: ')
        print(send_request(user_task, shop, store))


if __name__ == '__main__':
    main()
