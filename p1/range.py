# Range

# for one_number in range (1,5):
#     print(one_number)

# Range s kroky
# for one_number in range (1,10, 2):
#     print(one_number)

# Suma sudých čísel
suma = 0
for one_number in range (1,101):
    if one_number % 2==0:
        suma += one_number
    else:
        pass

print(suma)