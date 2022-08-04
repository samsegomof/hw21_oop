import pytest

from classes import Shop, Store


@pytest.fixture()
def shop():
    return Shop()


@pytest.fixture()
def store():
    return Store()


@pytest.fixture()
def items_2():
    return [('зерно', 2), ('яблоки', 4)]


@pytest.fixture()
def remove_items2():
    return [('зерно', 2), ('яблоки', 6)]


@pytest.fixture()
def items_2_dict():
    return {'зерно': 2, 'яблоки': 4}


@pytest.fixture()
def items_6():
    return [('зерно', 2), ('яблоки', 4), ('хлеб', 1), ('молоко', 1), ('кефир', 1), ('бананы', 1)]


@pytest.fixture()
def items_120():
    return [('зерно', 20), ('яблоки', 100)]
