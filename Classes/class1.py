class Dog:
    def __init__(self, name, age, listDog):
        self.name = name
        self.age = age
        self.listDog = []

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


d = Dog("bily", 14)
d.set_age(17)
print(d.get_age())
