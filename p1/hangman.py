# Hangman
import random
from hangman2 import stages
from hangman2 import words

print("Vítejte ve hře v hádání jmen z filmu Harry Potter")

# Generování náhodného slova
# words = ["harry", "ronald", "albus", "hermiona"]
random_word = words[random.randint(0,len(words)-1)]
# print(random_word)
# Generování podtržítek
hidden_word = []
for one_letter in random_word:
    hidden_word.append("_")

# Životy
lives = 6
print(stages[lives])

# Vypsání slova s podtržítky  normální podobě
printedWord = ""
for one_letter in hidden_word:
    printedWord += one_letter
print(printedWord)

while "_" in hidden_word:
    guess = input("Zadejte hádané písmeno?\n").lower()
    for index in range(0, len(random_word)):
        if guess == random_word[index]:
            hidden_word[index] = guess
        
    # kontrola životů
    if guess not in random_word:
        lives -= 1
        print(stages[lives])
    print(f"Počet vašich životů je {lives}")
    if lives == 0:
        print("Prohráli jste")
        break

# Vypsání slova s podtržítky  normální podobě
    printedWord = ""
    for one_letter in hidden_word:
        printedWord += one_letter
    print(printedWord)

# kontrola vítězství
if "_" not in hidden_word:
    print("Vyhráli jste!")

