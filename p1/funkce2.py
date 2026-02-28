import math
# Hodnoty od uživatele
height = int(input("Jaká je výška zdi? \n"))
width = int(input("Jaká je šířka zdi? \n"))
cans = int(input("Kolik pokryje jedna plechovka m^2 \n"))
# Funkce
def area (height, width, cans):
    area = height * width
    numbers_of_cans = math.ceil(area / cans)
    print(f"Zeď má {area} m^2 a budete potřebovat {numbers_of_cans} plechovek barvy.")
# Výpočet
area(height, width, cans)