import datetime

from Customer import Customer
from Product import Product
from Staff import Staff
from Store import Store


class Order:
    __slots__ = '__store', '__customer', '__staff', '__products', '__quantity'

    def __init__(self, store: Store, customer: Customer, staff: Staff, products: dict = {}, quantity=0):
        self.__quantity = quantity
        self.__products = products
        self.__staff = staff
        self.__customer = customer
        self.__store = store

    @property
    def quantity(self):
        return self.__quantity

    @property
    def products(self):
        return self.__products

    @property
    def staff(self):
        return self.__staff

    @property
    def customer(self):
        return self.__customer

    @property
    def store(self):
        return self.__store

    def add_product(self, product: Product):
        if product in self.products:
            self.__products[product] += 1
            self.__quantity += 1
        else:
            self.__products[product] = 1
            self.__quantity += 1

    def print_receipt(self):
        date = datetime.datetime.now()

        receipt = '\tWelcome to {5} - IUT\n' \
                  '\t\tStaff:{0}\n' \
                  '\t\tCustomer ID:{1}\n' \
                  '\n' \
                  '\t\t\tRECEIPT\n' \
                  '\t\t{2}\n' \
                  '\t\t{3}\n' \
                  '\t\tST # {4}\n' \
                  'Product Name\t\t\tProduct Code\tPrice\tQ\n'\
            .format(self.staff.name, self.staff.ID, date.date(), date.time(), self.store.ID, self.store.name)

        total_price = 0
        total_points = 0
        for product in self.products:
            receipt += '\n{0}\t\t\t{1}\t\t{2}\t{3}'.format(product.name, product.product_code, product.price, self.products[product])
            total_price += product.price * self.products[product]
            total_points += product.points * self.products[product]

        receipt += "\n\n\tTOTAL\t\t\t\t\t{0}\n" \
                   "\n\tTotal Points: {1}\n" \
                   "\t\t***CUSTOMER COPY***".format(total_price, total_points)
        self.customer.purchasing_points += total_points
        print(receipt)
