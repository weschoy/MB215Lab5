class Car:

    def __init__(self, sYear, sMake):
        self.__year_model=sYear
        self.__make=sMake
        self.__speed=0

    def accelerate (self):
        self.__speed+=5

    def brake (self):
        self.__speed-=5

    def get_speed (self):
        return self.__speed


sYear=input("Enter the car's year model: ")
sMake=input("Enter the make of the car: ")        

user_car=Car(sYear,sMake)

for i in range (0,5):
    user_car.accelerate() 
    speed=user_car.get_speed()
    print(speed," km/hr")

for i in range (0,5):
    user_car.brake()
    speed=user_car.get_speed()
    print(speed," km/hr")
