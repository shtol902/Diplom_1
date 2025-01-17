import pytest

from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

@pytest.fixture()
def mock_bun():
    mock_bun = Mock(Bun)
    mock_bun.get_price.return_value = 100
    mock_bun.get_name.return_value = 'Булка'
    return mock_bun

@pytest.fixture
def mock_sauce():
    mock_sauce = Mock(Ingredient)
    mock_sauce.get_price.return_value = 10
    mock_sauce.get_name.return_value = 'Кетчуп'
    mock_sauce.get_type.return_value = 'Соус'
    return mock_sauce


@pytest.fixture()
def mock_filling():
    mock_filling = Mock(Ingredient)
    mock_filling.get_price.return_value = 15
    mock_filling.get_name.return_value = 'Сыр'
    mock_filling.get_type.return_value = 'Начинка'
    return mock_filling


