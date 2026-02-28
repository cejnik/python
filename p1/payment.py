import random

names = input("Napiš mi jména všech, ale oddělené čárkou. \n")
list_people = names.split(", ")
random_payments = random.randint(0,len(list_people)-1)
print(f"Dneska bude platit {list_people[random_payments]}")