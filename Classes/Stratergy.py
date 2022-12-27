"""
-The strategy method is Behavioral Design pattern that allows you to define the complete family of algorithms, 
-encapsulates each one and putting each of them into separate classes and also allows to interchange there objects. 

"""


class Mario:
    def __init__(self, attack):
        self.attack = attack

    def setattack(self):
        self.attack


class attackStratergy(Mario):
    def attack(self, fire, water):
        self.fire = fire
        self.water = water


class NormalAttack(attackStratergy):
    def water(self, water):
        return water


class FireAttack(attackStratergy):
    def fire(self, fire):
        return fire


def main():
    Mario = Mario()
    Mario.attackStratergy = NormalAttack()


main()
