"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import *
from src.phone import Phone

# Создание экземпляров класса Item
obj1 = Item('Планшет', 10000, 2)
obj2 = Item('Телефон', 5000, 100)
obj3 = Item('SSD', 5000, 3)

# Задаем кофициенты повышения ЗП
obj1.pay_rate = 0.5
obj2.pay_rate = 0.8


# TestCase1


# Проверяем, что класс создан
def test_create_class():
    assert obj1.name == 'Планшет'
    assert obj1.price == 10000
    assert obj1.quantity == 2
    assert obj2.name == 'Телефон'
    assert obj2.price == 5000
    assert obj2.quantity == 100


# Тест метода calculate_total_price
def test_calculate_total_price():
    assert obj1.calculate_total_price() == 20000.0
    assert obj2.calculate_total_price() == 500000.0


# Тест метода apply_discount
def test_apply_discount():
    obj1.apply_discount()
    assert obj1.price == 5000.0

    obj2.apply_discount()
    assert obj2.price == 4000.0


# TestCase2
# Проверка сеттера атрибута name
def test_name_setter():
    obj1.name = 'Notebook'
    assert obj1.name == 'Notebook'


# Проверка при задании name более 10 символов
def test_name_setter__more_10_symbols():
    with pytest.raises(Exception):
        obj1.name = 'NotebookSony'


# Проверка работы класс-метода instantiate_from_csv
def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[1].price == '1000'


# Проверка работы статик-метода string_to_number
def test_string_to_number():
    assert Item.string_to_number('5.2') == 5


# TestCase3
# Проверка метода repr
def test_repr():
    assert repr(obj3) == "Item('SSD', 5000, 3)"


# Проверка метода str
def test_str():
    assert str(obj3) == 'SSD'


# TestCase4 - Тестирование метода add

obj_phone = Phone('Телефон', 10000, 4, 2)   # Создаем экземпляр класса Phone


def test_add():
    assert obj1 + obj2 == 102
    assert obj1 + obj_phone == 6
    assert obj2 + 5 is None
