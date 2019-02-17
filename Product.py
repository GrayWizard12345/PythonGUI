class Product:
    __slots__ = '__product_code', '__name', '__description', '__price', '__points'

    def __init__(self, product_code:int, name:str, description:str, price:float, points:int):
        self.__points = points
        self.__price = price
        self.__description = description
        self.__name = name
        self.__product_code = product_code

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value: int):
        self.__points = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        self.__price = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def product_code(self):
        return self.__product_code

    @product_code.setter
    def product_code(self, value: int):
        self.__product_code = value

    def __str__(self):
        return "Product Code:\t\t\t{0}\n" \
             "Name:\t\t\t\t\t{1}\n" \
             "Description:\t\t\t{2}\n" \
             "Price:\t\t\t\t\t{3}\n" \
             "Points\t\t\t\t\t{4}".format(self.product_code, self.name, self.description, self.price, self.points)
