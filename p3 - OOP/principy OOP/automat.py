from source_data import MENU
from source_data import resources

# === Základní nástavení ===
espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]


# ==== Funkce ===
def report(data):
    print(f"Voda: {data['water']}")
    print(f"Mléko: {data['milk']}")
    print(f"Káva: {data['coffee']}")

def coins():
    print("Prosím vložte mince 1,2,5,10,20 a 50.")
    kc1 = int(input("Kolik 1 kč chcete vložit? "))
    kc2 = int(input("Kolik 2 kč chcete vložit? ")) * 2
    kc5 = int(input("Kolik 5 kč chcete vložit? ")) * 5
    kc10 = int(input("Kolik 10 kč chcete vložit? ")) * 10
    kc20 = int(input("Kolik 20 kč chcete vložit? ")) * 20
    kc50 = int(input("Kolik 50 kč chcete vložit? ")) * 50
    suma = kc1 + kc2 + kc5 + kc10 + kc20 + kc50
    print(f"Celkem jste vložili {suma} Kč.")
    return suma

def calculate_change(user_sum_coins, price):
    refund = user_sum_coins - price
    if refund >= 0:
        print("Nápoj se připravuje. ")
        if refund > 0:
            print(f"Zde jsou peníze zpět {refund} Kč")
    else:
        print(f"Nevložili jste dostatek peněz. Ještě je zapotřebí vložit {price - user_sum_coins} Kč. ")

def fill_in_ingredience():
    return resources

def consumption_in(name_of_drink, ingredience):
    ingredience["water"]  -= MENU[name_of_drink]["ingredients"]["water"]
    ingredience["milk"]  -= MENU[name_of_drink]["ingredients"]["milk"]
    ingredience["coffee"]  -= MENU[name_of_drink]["ingredients"]["coffee"]
    print(f"Zbylé ingredience jsou {rest_of_ingredience}")


def calculate_ingrediencets(drink_name):
    if drink_name =="espresso":
        consumption_in(drink_name, rest_of_ingredience)
    elif drink_name =="latte":
        consumption_in(drink_name, rest_of_ingredience)
    elif drink_name =="cappuccino":
        consumption_in(drink_name, rest_of_ingredience)
        

def ingredience_checker(in_water, in_milk, in_coffee):
    if in_water < 0:
        print("Nemáme dostatek ingrediencí na tento nápoj")
        return False
    elif in_milk < 0:
        print("Nemáme dostatek ingrediencí na tento nápoj")
        return False
    elif in_coffee < 0:
        print("Nemáme dostatek ingrediencí na tento nápoj")
        return False
    else:
        print("Na váš nápoj máme dostatek informací.")
        return True

# === Kód automatu ===
rest_of_ingredience = fill_in_ingredience()

lets_continue = True
while(lets_continue):
    
    user_choice = input("Co byste si dal? (espresso/latte/cappuccino): ")
    # Výpočet zbývajích ingrediencí
    calculate_ingrediencets(user_choice)

    # Checker
    if user_choice != "report":
        lets_continue = ingredience_checker(rest_of_ingredience["water"], rest_of_ingredience["milk"], rest_of_ingredience["coffee"])
    
    # Má kód dále pokračovat
    if lets_continue == False:
        break

    if user_choice == "report":
        report(rest_of_ingredience)

    if user_choice == "espresso":
        sum = coins()
        print(f"Cena espressa je: {espresso_price}")
        calculate_change(sum, espresso_price)
    elif user_choice == "latte":
        sum = coins()
        print(f"Cena espressa je: {latte_price}")
        calculate_change(sum, latte_price)
    elif user_choice == "cappucino":
        sum = coins()
        print(f"Cena espressa je: {cappuccino_price}")
        calculate_change(sum, cappuccino_price)

