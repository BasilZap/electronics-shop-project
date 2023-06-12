from src.item import Item


class Mixin:

    def __init__(self, name, price, quantity, language):
        super().__init__(name, price, quantity)
        self.language = language

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"


class Keyboard(Mixin, Item):
    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity, language)

