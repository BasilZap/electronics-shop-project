import pytest
from src.phone import Phone

# TestCase4

# Создание экземпляров класса Phone
obj_phone1 = Phone('Телефон', 80000, 4, 2)
obj_phone2 = Phone('Nokia', 1000, 200, 1)


# Проверяем, что класс создан
def test_init_phone():
    assert obj_phone1.name == 'Телефон'
    assert obj_phone1.price == 80000
    assert obj_phone1.quantity == 4
    assert obj_phone1.number_of_sim == 2


# Тестируем метод repr класса Phone
def test_repr_phone():
    assert repr(obj_phone2) == "Phone('Nokia', 1000, 200, 1)"


# Тестируем сеттер количества сим-карт класса Phone
def test_number_of_sim():
    obj_phone2.number_of_sim = 2
    assert obj_phone2.number_of_sim == 2


# Тестируем проверку количества сим-карт класса Phone
def test_number_of_sim__more_0():
    with pytest.raises(Exception):
        obj_phone1.number_of_sim = 0

