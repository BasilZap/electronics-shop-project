from src.item import Item


# Создание класса Mixin
class Mixin:
    Language = "EN"

# Конструктор класса
    def __init__(self):
        self.__language = self.Language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Функция класса Mixin, которая изменяет раскладку
        клавиатуры и возвращает класс Mixin с изменениями
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


# Объявление класса клавиатуры
class Keyboard(Item, Mixin):
    pass

