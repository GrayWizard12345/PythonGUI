class Staff:
    _job_title: str
    _name: str
    __slots__ = '__ID', '__ssn', '__name', '__job_title'

    def __init__(self, ID, ssn, name, job_title):
        self.__job_title = job_title
        self.__name = name
        self.__ssn = ssn
        self.__ID = ID

    @property
    def job_title(self):
        return self.__job_title

    @property
    def name(self):
        return self.__name

    @property
    def ssn(self):
        return self.__ssn

    @property
    def ID(self):
        return self.__ID

    @name.setter
    def name(self, value: str):
        self.__name = value

    @ssn.setter
    def ssn(self, value: str):
        self.__ssn = value

    @ID.setter
    def ID(self, value: int):
        self.__ID = value

    @job_title.setter
    def job_title(self, value: str):
        self.__job_title = value

    def __str__(self):
        return "\t\tStaff Member Info\n" \
               "ID:\t\t\t\t\t{0}\n" \
               "Name:\t\t\t\t{1}\n" \
               "SSN:\t\t\t\t{2}\n" \
               "JOB_TITLE:\t\t\t{3}".format(self.ID, self.name, self.ssn, self.job_title)
