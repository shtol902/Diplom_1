import pytest

from praktikum.database import Database

class TestDatabase:
    def test_available_buns_have_all_bun(self):
        all_buns = Database()
        assert len(all_buns.available_buns()) == 3

    def test_available_ingredients_have_all_ingredients(self):
        all_ingredients = Database()
        assert len(all_ingredients.available_ingredients()) == 6