"""
inheritance 

"""
# this is Generalised class called generalisation.
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

    def speak(self):
        print("I don't know what I say")


# this is specific classes.
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("bark")


p = Pet("Tim", 7)
p.speak()
c = Cat("Bill", 8, "brown")
c.show()
d = Dog("Jill", 12)
d.speak()
