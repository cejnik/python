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

    


user_name = input("Jaké bude vaše jméno ve hře? ")
age = int(input("Jaký bude váš věk? "))


player1 = WizzardPlayer(user_name,age)
player1.age_checker()
player1.attack()
print(player1.wizzard_club)

# help(player1)

# print(player1.name)