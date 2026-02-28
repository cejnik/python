# Hádací hra
import random
print(f"Vítejte ve hře o Harry Potterovi.")
characters = ["Harry", "Ron", "Hermiona", "Draco", "Crabbe", "Goyle", "Albus"]
character = characters[random.randint(0, len(characters)-1)]
guess = ""
rounds = 5


while character != guess:
    if rounds != 0:
        guess = input("Uhodněte postavu z filmu Harry Potter: \n")
        rounds -= 1
    else:
        print("Došli ti pokusy, prohrál jsi.")
        break
    if character == guess:
        print(f"Vyhrál jsi!. Hádané slovo bylo {character}")