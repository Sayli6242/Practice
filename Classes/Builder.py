"""
"""


class Pizza:
    def __init__(self):
        self.base = 0
        self.time = 0
        self.toppings = []

    def setbase(self, base):
        self.base = base

    def settime(self, time):
        self.time = time

    def settoppings(self, toppings):
        self.toppings = toppings

    def print(self):
        print(self.base, self.time, self.toppings)


class Cook:

    # def __init__(self, Pizza):
    #     self.Pizza = Pizza

    def base():
        pass

    def time():
        pass

    def toppings():
        pass

    def prepare():
        pass

    def deliver():
        pass


class italianCook(Cook):
    def __init__(self, Pizza):
        self.Pizza = Pizza

    def base(self):
        self.Pizza.setbase(10)

    def time(self):
        self.Pizza.settime(15)

    def toppings(self):
        self.Pizza.settoppings(["a", "b"])

    def deliver(self):
        self.prepare()
        return self.Pizza

    def prepare(self):
        self.base()
        self.time()
        self.toppings()


class mexicanCook(Cook):
    def __init__(self, Pizza):
        self.Pizza = Pizza

    def base(self):
        self.Pizza.setbase(5)

    def time(self):
        self.Pizza.settime(10)

    def toppings(self):
        self.Pizza.settoppings(["c", "d"])

    def deliver(self):
        self.prepare()
        return self.Pizza

    def prepare(self):
        self.base()
        self.time()
        self.toppings()


class HeadChef:
    def __init__(self):
        pass

    def setCook(self, cook):
        self.cook = cook

    def getPizza(self):
        return self.cook.deliver()


def main():
    p1 = Pizza()
    p2 = Pizza()
    ic = italianCook(p1)
    mc = mexicanCook(p2)
    hc = HeadChef()
    hc.setCook(mc)
    finished_pizza1 = hc.getPizza()
    finished_pizza1.print()

    hc.setCook(ic)
    finished_pizza2 = hc.getPizza()
    finished_pizza2.print()


main()
