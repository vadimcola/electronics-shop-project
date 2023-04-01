"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


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


def test_instantiate_from_csv():
    Item.instantiate_from_csv('./src/items.csv')
    try:
        Item.instantiate_from_csv('./src/items_break.csv')
    except InstantiateCSVError:
        print('Файл item.csv поврежден')
    try:
        Item.instantiate_from_csv('../src/items.csv')
    except FileNotFoundError:
        print("Отсутствует файл item.csv")


def test_magical_methods(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


def test_add():
    item2 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item2 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(ValueError):
        phone1 + 1000


def test_InstantiateCSVError():
    error = InstantiateCSVError()
    assert error.__str__() == "Файл item.csv поврежден"

