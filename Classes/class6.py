"""dummy example"""


# class car:
#     def __init__(self,model,year,brand):
#         self.model = model
#         self.year = year
#         self.brand = brand

#     def set_parameters(self):
       
#         self.model = input("enter model name")
#         self.year = input("enter the year")
#         self.brand = input("enter care brand")

# car = car(model, year, brand)
# car.set_parameters()
# print(car.model)

# print(car.year)
# print(car.brand)

class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.year = None

    def start_engine(self):
        print("Engine started!")

    def set_parameters(self):
        self.brand = input("Enter the brand: ")
        self.model = input("Enter the model: ")
        self.year = input("Enter the year: ")

car = Car()
car.set_parameters()

print(car.brand)
print(car.model)
print(car.year)
