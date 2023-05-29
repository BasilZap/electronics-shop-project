"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import *

obj1 = Item('Планшет', 10000, 2)
obj2 = Item('Телефон', 5000, 100)

obj1.pay_rate = 0.5
obj2.pay_rate = 0.8


def test_create_class():
    assert obj1.name == 'Планшет'
    assert obj1.price == 10000
    assert obj1.quantity == 2
    assert obj2.name == 'Телефон'
    assert obj2.price == 5000
    assert obj2.quantity == 100


def test_calculate_total_price():
    assert obj1.calculate_total_price() == 20000.0
    assert obj2.calculate_total_price() == 500000.0


def test_apply_discount():
    obj1.apply_discount()
    assert obj1.price == 5000.0

    obj2.apply_discount()
    assert obj2.price == 4000.0


# TestCase2

def test_name_setter():
    obj1.name = 'Notebook'
    assert obj1.name == 'Notebook'


def test_name_setter__more_10_symbols():
    with pytest.raises(Exception):
        obj1.name = 'NotebookSony'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[1].price == '1000'


def test_def_string_to_number():
    assert Item.string_to_number('5.2') == 5
