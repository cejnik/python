# print (9 % 2)
# cislo = int(input("Zadejte celé číslo?"))
# if cislo % 2 == 0:
#     print("Jedná se o sudé číslo")
# else:
#     print("Jedná se o liché číslo")

# BMI
height = float(input("Kolik měříš?\n"))
weight = float(input("Kolik vážíš?\n"))

bmi = weight / height**2

print(round(bmi,1))

if bmi <= 18.5:
    print(f"Jsi pohublí a máš hodnotu {bmi}")
elif bmi <= 24.9:
    print(f"Máš normální BMI a máš hodnotu {bmi}")
elif bmi <= 29.9:
    print(f"Máš lehkou nadváhu a máš hodnotu {bmi}")
elif bmi <= 34.9:
    print(f"Jsi obézní a máš hodnotu {bmi}")
else:
    print(f"Jsi morbidně obézní a máš hodnotu {bmi}")



