# Atributy(vlastnosti, proměnné) a metody(činnost,funkce)
class WizzardPlayer:

    wizzard_club = True

    def __init__(self, name="anonym", age=0):
        if age >= 18:
            self.name = name
            self.age = age

    def attack(self):
        print("Útok")

    def age_checker(self):
        if self.age >= 18:
            print("Můžete hrát.")
        else:
            print("Nemůžete hrát.")
   
     # Není vazaná na objekty, ale na classu
    @staticmethod
    def test_function(n1, n2):
        return n1 + n2
    # vrací objekt
    @classmethod
    def test_function2(cls, n1, n2):
        return cls("Harry", n1+n2)

# player1 = WizzardPlayer("Martin", 30)
# print(WizzardPlayer.test_function(60,100))
test_player = WizzardPlayer.test_function2(30,40)
print(test_player.name)
print(test_player.age)