class Product:
    def __init__(self, name, price, weight):
        self.__name = self.__validate_name(name)
        self.__price = self.__validate_price(price)
        self.__weight = self.__validate_weight(weight)

        assert isinstance(
            self.__name, str), 'Название товара не является строкой'
        assert all(isinstance(data, (int, float)) for data in (
            self.__price, self.__weight)), 'Неправильный тип данных у цены или веса товара'

    def __str__(self) -> str:
        return f'{self.__name}'

    @staticmethod
    def __validate_name(name):
        if not isinstance(name, str):
            raise ValueError('Название товара должно быть строкой')
        elif len(name.split()) > 5:
            raise ValueError('В названии товара должно быть не больше 5 слов')
        elif len(name) < 2 or len(name) > 100:
            raise ValueError(
                'Длина названия товара не может быть меньше 2 символов и не больше 100')
        return name

    @staticmethod
    def validate_type_number(number, error_msg):
        if not isinstance(number, (int, float)):
            raise ValueError(error_msg)

    @classmethod
    def __validate_price(cls, price):
        cls.validate_type_number(
            price, 'Цена должна быть должна быть целым числом')
        if price <= 0:
            raise ValueError('Цена товара не можеть быть меньше или равна 0')
        return price

    @classmethod
    def __validate_weight(cls, weight):
        cls.validate_type_number(weight, 'Вес должен быть числом')
        if weight < 0.001 or weight > 100:
            raise ValueError(
                'Вес товара должен быть не меньше 0.001кг и не больше 100 кг')
        return weight

    @property
    def get_weight(self):
        return self.__weight

    @property
    def get_price(self):
        return self.__price

    @property
    def get_name(self):
        return self.__name


class Buy(Product):
    def __init__(self, name, price, weight, quantity):
        super().__init__(name, price, weight)
        self.__quantity = self.__validate_quantity(quantity)
        self.__total_weight, self.__total_price = self.__total_cost_weight_package()
        
        assert self.__quantity > 1 and self.__quantity < 1000, 'Ошибка в количестве товара'

    @classmethod
    def __validate_quantity(cls, quantity):
        cls.validate_type_number(quantity, 'Количество должно быть числом')
        if quantity < 1 or quantity > 1000:
            raise ValueError(
                'Пользователь не может заказать товар в количестве меньше 1 и больше 1000')
        return quantity

    def __total_cost_weight_package(self):
        total_weight = self.get_weight * self.__quantity
        total_price = self.get_price * self.__quantity
        assert total_price > 0 , 'Цена не может быть меньше 0 или равно ему'
        assert total_weight > self.get_weight, 'Итоговый вес не может быть равен изначальному'
        return total_weight, total_price

    def __str__(self) -> str:
        cost_weight = self.__total_cost_weight_package()
        return f'{self.get_name} - {cost_weight[0]} - {cost_weight[1]}'

    @property
    def get_quantity(self):
        return self.__quantity

    @property
    def get_total_weight(self):
        return self.__total_weight

    @property
    def get_total_price(self):
        return self.__total_price


class Check(Buy):
    def __init__(self, name, price, weight, quantity):
        super().__init__(name, price, weight, quantity)

    def __str__(self):
        return f'''Товар: {self.get_name}
                Количество: {self.get_quantity}
                Итоговый вес: {self.get_total_weight} 
                Итоговая стоимость: {self.get_total_price}'''


purchases_check = [Buy('Книга', 700, 0.2, 2), Check(
    'Диван', 20000, 100, 5), Check('Стол', 5000, 50, 2)]


for purchase in purchases_check:
    print(purchase)
