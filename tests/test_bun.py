import pytest
import data

from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize('name, price', data.buns.items())
    def test_get_name_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', data.buns.items())
    def test_get_price_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price