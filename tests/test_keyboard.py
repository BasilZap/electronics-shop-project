import pytest
from src.keyboard import Keyboard, Mixin

# TestCase5

# Создание экземпляра класса Keyboard

key = Keyboard("Genius", 500, 30)


# Тестируем создание экземпляра класса Keyboard
def test_init_keyboard():
    assert key.name == "Genius"
    assert key.price == 500
    assert key.quantity == 30
    assert key.language == "EN"


# Тестируем функцию изменения языка класса Keyboard
def test_keyboard_change_lang():
    key.change_lang()
    assert key.language == "RU"
    key.change_lang().change_lang()
    assert key.language == "RU"


# Тестируем возможность задания раскладки напрямую
def test_language__set_property():
    with pytest.raises(Exception):
        key.language = "KZ"
