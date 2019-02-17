from Customer import Customer
from Order import Order
from Product import Product
from Staff import Staff
from Store import Store

if __name__ == "__main__":

    c1 = Customer("01223", "Peter Parker", "Qo'yliq", 2.2, "90-932-75-98", ["Silver", 'Gold'])
    c2 = Customer("01223", "Sherlock Holmes", "Backer street", 31415, "90-987-65-43", ["Regular", 'VIP'])
    store = Store('U1510375', "John's Mall", "Ziyolar-9", "90-123-45-67")
    staff1 = Staff("0", "02213", "Uncle Ben", "Manager")
    staff2 = Staff("1", "45646", "Aunt May", "Cashier")
    staff3 = Staff('2', "12345", "John Doe", "Owner")
    p1 = Product(69, "Cucumber", "Fresh and long cucumber", 69.69, 666)
    p2 = Product(666, "Tomatoes", "Red and plump", 12.14, 314)
    order = Order(store, c1, staff2)

    print(store)
    print()
    print(c1)
    print()
    print(c2)
    print()
    print(staff1)
    print()
    print(staff2)
    print()
    ans = 0
    while ans != "yes":
        print("Are you ready to make an order? (type yes or no):")
        ans = input()
        if ans == "no":
            print("Okay, type yes when you'll be ready!")

    while ans != 'done':
        print("Currently there are only 2 products:\n"
              "1. Cucumber\n"
              "2. Tomatoes\n"
              "Which one do you want to by?: (type 1 or 2 or 'done' to proceed)")
        ans = input()
        if ans == '1':
            order.add_product(p1)
        if ans == '2':
            order.add_product(p2)
    print("\tHere is your receipt:\n")
    order.print_receipt()

