import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
 
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
 
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
all_list = [rock, paper, scissors]
player_choice = int(input("Vyber si kámen, nužky papír. Kámen je 0, papír 1 a nůžky 2"))
user_picture = all_list [player_choice]
computer_choice = random.randint(0,2)
computer_picture = all_list[computer_choice]
print(f"uživatel si vybral {user_picture}\n")
print(f"Počítač si vybral {computer_picture}\n")

# if player_choice == computer_choice:
#     print("Remíza")
# elif player_choice == 0 and computer_choice == 1:
#     print("Počítač vyhral, prohrál jsi")
# elif player_choice == 0 and computer_choice == 2:
#     print("Vyhrál jsi, počítač prohrál.")
# elif player_choice == 1 and computer_choice == 0:
#     print("Vyhrál jsi, počítač prohrál.")
# elif player_choice == 1 and computer_choice == 2:
#     print("Počítač vyhral, prohrál jsi")
# elif player_choice == 2 and computer_choice == 0:
#     print("Počítač vyhral, prohrál jsi")
# elif player_choice == 2 and computer_choice == 1:
#     print("Vyhrál jsi, počítač prohrál.")

# Druhá varianta
if player_choice == computer_choice:
    print("Remíza")
elif player_choice == 0 and computer_choice == 1 or player_choice == 1 and computer_choice == 2 or player_choice == 2 and computer_choice == 0:
    print("Počítač vyhral, prohrál jsi")
elif player_choice == 0 and computer_choice == 2 or player_choice == 1 and computer_choice == 0 or player_choice == 2 and computer_choice == 1:
    print("Vyhrál jsi, počítač prohrál.")