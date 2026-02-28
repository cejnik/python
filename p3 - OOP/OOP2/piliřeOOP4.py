# Atributy(vlastnosti, proměnné) a metody(činnost,funkce)
# 1. pilíř: Encapsulation = zapouzdření
# 2. pilíř: abstraction = dáváme přístup pouze k timu, co je zapotřebí. Když je tam _, neměním funkce ani na to nesahám
# 3. pilíř: Inheritance = dělení
# 4. pilíř: Polymorfish = mnohoforem

# FUnkce super rozšiřuje původní konstruktor.
class WizzardPlayer:

    wizzard_club = True

    def __init__(self, name="anonym", age=0):
        if age >= 18:
            self.name = name
            self.age = age

    def attack(self):
        return "Útok 1. stupně"

    def age_checker(self):
        if self.age >= 18:
            print("Můžete hrát.")
        else:
            print("Nemůžete hrát.")

class HeadWizzard(WizzardPlayer):
    # Super
    def __init__(self, name, age, typ):
        super().__init__(name, age)
        self.typ = typ


    def attack(self):
        return "Útok 2. stupně"
    def adava_kedavra(self):
        return "Avada_kedavra!"
   
player_1 = WizzardPlayer("Martin", 30)
player_2 = HeadWizzard("Kristýna", 31, "good")

# print(player_1.name)
# print(player_1.age)
# print(player_1.attack())
# print("-------------------------------------")
# print(player_2.name)
# print(player_2.age)
# print(player_2.attack())
# print(player_2.adava_kedavra())
# print("-------------------------------------")

# # Kontrola instance, za se player1 vytváří wizzardPlayer
# print(isinstance(player_1, WizzardPlayer))
# print(isinstance(player_2, WizzardPlayer))

# print(player_1.attack())
# print(player_2.attack())

# print(player_2.name)
# print(player_2.age)
# print(player_2.typ)


# Introspection ->
# print(dir(player_2))
# # Funkce dir
# print("-------------------------------------")
# print(player_2.__dir__())
# Metoda dir

# print(str(player_2))
# print(player_2.__str__())


# Method Resolution Order = MRO -> ukazuje, co a jak dětí a jakým to jde hyearchicky za sebou.
print(HeadWizzard.mro())
print(HeadWizzard.__mro__)
print(WizzardPlayer.mro())
print(WizzardPlayer.__mro__)





# Dunder Methods -> všechny, které začínají __

