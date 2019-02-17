class Store:
    __slots__ = '__ID', '__name', '__address', '__tel'

    def __init__(self, ID:str, name:str, address:str, tel:str):
        self.__ID = ID
        self.__tel = tel
        self.__address = address
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def ID(self):
        return self.__ID

    @property
    def address(self):
        return self.__address

    @property
    def tel(self):
        return self.__tel

    @address.setter
    def address(self, value):
        if isinstance(value, str):
            self.__address = value
        else:
            raise AttributeError

    @tel.setter
    def tel(self, value):
        if isinstance(value, int):
            self.__tel = value
        else:
            raise AttributeError

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise AttributeError

    @ID.setter
    def ID(self, value):
        if isinstance(value, int):
            self.__ID = value
        else:
            raise AttributeError

    def __str__(self):
        return "\t\t{1}\n" \
               "ID:\t\t\t\t{0}\n" \
               "Address:\t\t{2}\n" \
               "Tel:\t\t\t{3}".format(self.ID, self.name, self.address, self.tel)
