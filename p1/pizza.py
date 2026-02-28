print("Vítejte v aplikaci na objednání pizzy.")
size = str(input("Jakou si dáš pizzu? S, M nebo L? "))
pfefer = str(input("Chceš k tomu feferonky? A/N? "))
cheese = str(input("Chceš k tomu sýr navíc? A/N? "))

pizza_bill = 0

if size == "S":
    pizza_bill += 100
elif size == "M":
    pizza_bill += 150
elif size == "L":
    pizza_bill += 200

if pfefer == "A":
    if size != "S":
        pizza_bill += 30
    else:
        pizza_bill += 20

if cheese == "A":
    pizza_bill += 15

print(f"Částka k zaplacení bude {pizza_bill} kč.")