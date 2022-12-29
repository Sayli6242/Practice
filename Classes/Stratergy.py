"""
-The strategy method is Behavioral Design pattern that allows you to define the complete family of algorithms, 
-encapsulates each one and putting each of them into separate classes and also allows to interchange there objects. 

"""

# should be composition
class Mario:
    def __init__(self, attack):
        self.attack = attack

    def setattack(self):
        self.attack


# blueprint
class attackStratergy:
    def do_attack(self, attack):
        pass


class NormalAttack(attackStratergy):
    def attack(self, water):
        self.attack = water


class FireAttack(attackStratergy):
    def fire(self, fire):
        self.attack = fire


def main():
    Mario = Mario()
    Mario.attackStratergy = NormalAttack()


main()
