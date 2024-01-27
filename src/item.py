import csv


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
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

    def __repr__(self):
        """
        :return: 'Item'("Название", "Цена", "Количество")
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        :return: Название товара
        """
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return None

    def calculate_total_price(self) -> int:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.pay_rate * self.quantity
        total_price_int = int(total_price)
        return total_price_int

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = str(name[0:10])

    @classmethod
    def instantiate_from_csv(cls, path_file: str) -> None:
        """
        Получает CSV-файл и отдаёт 5 классов
        """
        cls.all.clear()

        with open(path_file, 'r', encoding='UTF-8') as csv_file:
            file = csv.DictReader(csv_file)

            for row in file:
                cls(row['name'], float(row['price']), float(row['quantity']))

    @staticmethod
    def string_to_number(string) -> int:
        """
        Берёт число в формате str и возвращает в int
        """
        number = string.replace(',', '.')
        return int(float(number))
