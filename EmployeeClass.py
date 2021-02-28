class Employee:

    def __init__(self, sName, sIDNumber, sDepartment, sJobTitle):
        self.__Name=sName
        self.__ID=sIDNumber
        self.__Department=sDepartment
        self.__Job=sJobTitle

    def name(self):
        return self.__Name

    def ID(self):
        return self.__ID

    def Department(self):
        return self.__Department

    def Job(self):
        return self.__Job

    def __str__(self):
        return "Employee: " +self.__Name + "\n" + str(self.__ID) + "\n" + self.__Department + "\n" + self.__Job + "\n\n"


