import pytest as pytest

import tests.conftest
from classes import Request


class TestRequest:

    def test_create(self, shop, store):
        request = Request([shop, store], 'Доставить 3 печеньки из склад в магазин')
        assert request.from_ == 'склад', "Error in 'from' field"
        assert request.to == 'магазин', "Error in 'from' field"
        assert request.amount == 3, "Error in 'from' field"
        assert request.product == 'печеньки', "Error in 'product' field"
