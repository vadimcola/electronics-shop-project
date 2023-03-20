"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_init(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    assert item1.apply_discount() == 8500


def test_name_ok(item1):
    item1.name = "Телефон"
    assert item1.name == "Телефон"


def test_name_bed(item1):
    with pytest.raises(ValueError):
        item1.name = "СуперСмартфон"


def test_str_to_num():
    assert Item.string_to_number('9.2') == 9


def test_instantiate_from_csv(CSV_FILE='./src/items.csv'):
    assert type(Item.all) is not None

# def test_get_from_cvs():
#     Item.instantiate_from_csv(CSV_FILE='./src/items.csv')