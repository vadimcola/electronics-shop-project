import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []
    CSV_FILE = '../src/items.csv'

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            raise ValueError("Имя не должно превышать 10 символов")

    @classmethod
    def instantiate_from_csv(cls):
        with open(cls.CSV_FILE, encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name, price, quantity = row.get('name'), int(row.get('price')), int(row.get('quantity'))
                cls.all.append((name, price, quantity))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        return self.price * self.pay_rate

    @staticmethod
    def string_to_number(any_string: str) -> int:
        try:
            return int(any_string)
        except ValueError:
            return int(any_string[0: any_string.find('.')])


# Item.instantiate_from_csv()
# print(Item.all)
