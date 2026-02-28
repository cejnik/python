print("Vítejte na horské dráze")
height = int(input("Jaký je vaše výška v cm?\n"))
bill = 0

if height >= 87:
    print("Mužete jít na horskou dráhu")
    age = int(input("Jaký je Váš věk?"))
    if age < 12:
        bill = 50
        print("Lístek stojí 50 kč")
    elif age < 18:
        bill = 100
        print("Lístek stojí 100 kč")
    else:
        bill = 150
        print("Lístek stojí 150 kč")
    photo = input("Chceš fotku? ano/ne? \n")
    if photo == "ano":
        bill += 50
        print(f"Finální cena bude {bill} kč.")
    else:
        print(f"Celková cena bude {bill} kč.")      
else:
    print("Omlouvám se, ale na horské dráze nemuže jet.")