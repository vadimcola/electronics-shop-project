import pytest
from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_init(phone1):
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
