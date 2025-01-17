from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient

class TestBurger:
    def test_init_burger(self):
        burger = Burger()
        assert burger.bun is None
        assert len(burger.ingredients) == 0

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce


    def test_remove_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_filling

    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_filling
        assert burger.ingredients[1] == mock_sauce

    def test_get_price(self, mock_sauce, mock_filling, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        mock_ingredient_first = Mock(Ingredient)
        mock_ingredient_first.get_price.return_value = 10
        mock_ingredient_second = Mock(Ingredient)
        mock_ingredient_second.get_price.return_value = 15
        burger.add_ingredient(mock_ingredient_first)
        burger.add_ingredient(mock_ingredient_second)
        assert burger.get_price() == 225