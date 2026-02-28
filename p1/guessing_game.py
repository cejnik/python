# import random
# import os
# from guessing_game_logo import logo

# print("Vítejte ve hře guess secret number, Porazte počítač.")
# print("Myslím si číslo od 1 do 100")



# # Příprava hry
# secret_number = random.randint(1,100)
# print(f"Hádané číslo je {secret_number}")

# def difficulty():
#     difficulty = input("Vyberte obtížnost easy (10 životů) nebo hard (5 životů): ")
#     if difficulty == "easy":
#         return 10
#     elif difficulty == "hard":
#         return 5

# def guessing_game():
#     # Počet pokusů:
#     attems = difficulty()
#     another_game = ""
#     while attems > 0:
#         print(f"Váš počet zbývajících pokusů je {attems}")
#         guess = int(input("Tipněte si číslo? "))
#         print(f"Hádané číslo je {secret_number}")
#         if guess < secret_number:
#             print("Příliš nízké")
#             attems -= 1
#         elif guess > secret_number:
#             print("Příliš vysoké")
#             attems -= 1
#         else:
#             print("Vyhráli jste, počítač poražen!.")
#             another_game = input("Napište yes or no: ")
#         if attems == 0:
#             print("Prohráli jste, počítač vyhrál")
#             another_game = input("Napište yes or no: ")
#         if another_game =="yes":
#             os.system("cls")
#             guessing_game()
#         elif another_game =="no":
#             os.system("cls")
#             break


# guessing_game()


# Pokus č.2
import random
import os

def difficulty():
    while True:
        diff = input("Vyberte obtížnost easy (10 životů) nebo hard (5 životů): ").lower()
        if diff == "easy":
            return 10
        elif diff == "hard":
            return 5
        else:
            print("Neplatná volba.")

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = difficulty()

    while attempts > 0:
        print(f"Zbývající pokusy: {attempts}")
        guess = int(input("Tipněte si číslo: "))

        if guess < secret_number:
            print("Příliš nízké")
        elif guess > secret_number:
            print("Příliš vysoké")
        else:
            print("🎉 Vyhráli jste!")
            return

        attempts -= 1

    print(f"❌ Prohráli jste. Číslo bylo {secret_number}")

while True:
    os.system("cls")
    print("Vítejte ve hře Guess the Number!")
    guessing_game()

    again = input("Chcete hrát znovu? (yes/no): ").lower()
    if again != "yes":
        break
