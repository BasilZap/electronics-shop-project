import csv


CSV_FILE_PATH = './src/items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all = self.all.append(self)

    def __repr__(self):
        """
        Переопределение метода repr
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Переопределение метода str
        """
        return f"{self.__name}"

    def __add__(self, other):
        """
        Переопределение метода add для класса Item
        """
        if isinstance(other, Item):
            ret_val = self.quantity + other.quantity
            return ret_val
        return None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """
        Сеттер атрибута name с проверкой длины имени
        """
        if 10 >= len(new_name):
            self.__name = new_name
        else:
            raise Exception('Длина наименования товара превышает 10 символов')

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса `Item` данными из файла src/items.csv
        """
        cls.all.clear()
        with open(CSV_FILE_PATH, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(some_number: str) -> int:
        """
        Возвращение заданного числа в формате int
        """
        return int(float(some_number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
