import pytest as pytest

import tests.conftest
from classes.exceptions import WarehouseFull, ItemsNotFound


class TestShop:

    def test_create(self, shop):
        assert str(shop) == 'Это Storage типа Shop с емкостью 20', 'Ошибка при создании объекта shop'


class TestShopAdd:

    def test_add_okay(self, shop, items_2):
        for item in items_2:
            shop.add(*item)
        assert str(shop) == 'Это Storage типа Shop с емкостью 20', 'Ошибка при создании объекта shop'

    @pytest.mark.xfail()
    def test_add_titles_exceeded(self, shop, items_6):
        for item in items_6:
            shop.add(*item)
        raise WarehouseFull

    @pytest.mark.xfail()
    def test_add_capacity_exceeded(self, shop, items_120):
        for item in items_120:
            shop.add(*item)
        raise WarehouseFull


class TestShopAdd:

    def test_okay(self, shop, items_2):
        for item in items_2:
            shop.add(*item)

    @pytest.mark.xfail()
    def test_titles_exceeded(self, shop, items_6):
        for item in items_6:
            shop.add(*item)
        raise WarehouseFull

    @pytest.mark.xfail()
    def test_capacity_exceeded(self, shop, items_120):
        for item in items_120:
            shop.add(*item)
        raise WarehouseFull


class TestShopRemove():

    def test_okay(self, shop, items_2):
        for item in items_2:
            shop.add(*item)
        for item in items_2:
            shop.remove(*item)

    @pytest.mark.xfail()
    def test_title_not_found(self, shop, items_2, items_6):
        for item in items_2:
            shop.add(*item)
        for item in items_6:
            shop.remove(*item)
        raise ItemsNotFound

    @pytest.mark.xfail()
    def test_quantity_exceeded(self, shop, items_2, remove_items2):
        for item in items_2:
            shop.add(*item)
        for item in remove_items2:
            shop.remove(*item)
        raise ItemsNotFound


class TestShopGetItems():

    def test_dictionary(self, shop, items_2, items_2_dict):
        for item in items_2:
            shop.add(*item)
        assert shop.get_items() == items_2_dict
