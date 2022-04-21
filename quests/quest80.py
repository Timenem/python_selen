"""
You need to create the class Warrior , the instances of which will have 2 parameters - health (equal to 50 points) and attack (equal to 5 points), and 1 property - is_alive, which can be True (if warrior's health is > 0) or False (in the other case). In addition you have to create the second unit type - Knight, which should be the subclass of the Warrior but have the increased attack - 7. Also you have to create a function fight() , which will initiate the duel between 2 warriors and define the strongest of them. The duel occurs according to the following principle:
Every turn, the first warrior will hit the second and this second will lose his health in the same value as the attack of the first warrior. After that, if he is still alive, the second warrior will do the same to the first one.
The fight ends with the death of one of them. If the first warrior is still alive (and thus the other one is not anymore), the function should return True , False otherwise.
"""

class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        if self.health >= 0:
            print(f"{self.health} {'alive'}")
            return True
        else:
            print(f"{self.health} {'dead'}")
            return False

    def attack_enemy(self, enemy):
        if enemy.is_alive:
            self.health -= enemy.attack


class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        super().__init__(health, attack)
        self.health = health
        self.attack = attack


def fight(unit1: Warrior, unit2: Knight):
    while unit1.is_alive and unit2.is_alive:
        unit2.attack_enemy(unit1)
        unit1.attack_enemy(unit2)
    return unit1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
