class Customer:

    __slots__ = '__ssn', '__name', '__address', '__purchasing_points', '__tel', '__membership'

    def __init__(self, ssn, name, address, purchasing_points, tel, membership):
        self.__membership = membership
        self.__tel = tel
        self.__purchasing_points = purchasing_points
        self.__address = address
        self.__name = name
        self.__ssn = ssn

    @property
    def membership(self):
        return self.__membership

    @membership.setter
    def membership(self, value: list):
        self.__membership = value

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, value: str):
        self.__tel = value

    @property
    def purchasing_points(self):
        return self.__purchasing_points

    @purchasing_points.setter
    def purchasing_points(self, value: int):
        self.__purchasing_points = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        self.__address = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def ssn(self):
        return self.__ssn

    @ssn.setter
    def ssn(self, value: str):
        self.__ssn = value

    def _try(self):
        try:
            return self.__dict__
        except:
            return str(self)

    def __str__(self):
        str = "\t\tCustomer info:\n" \
              "Name:                   {0}\n" \
               "SSN:                    {1}\n" \
               "Address:                {2}\n" \
               "Purchasing points:      {3}\n" \
               "Tel:                    {4}".format(self.name, self.ssn, self.address, self.purchasing_points, self.tel)
        for i in self.membership:
            str += '\n' \
                   'Memebership at:         {0}'.format(i)
        return str
