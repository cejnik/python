import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']
print("Generátor hesel")
password__letters_lenght = int(input("Kolik písmen chcete mít ve svém heslu\n"))
password__number_lenght = int(input("Kolik čísel chcete mít ve svém heslu\n"))
password__special_char_lenght = int(input("Kolik speciálních znaků chcete mít ve svém heslu\n"))

# Písmena
result = []
for one_letter in range (0, password__letters_lenght):
    result.append(letters[random.randint(0, len(letters)-1)])
# Čísla
for one_number in range (0, password__number_lenght):
    result.append(numbers[random.randint(0, len(numbers)-1)])
# Speciální znaky
for one_char in range (0, password__special_char_lenght):
    result.append(special_char[random.randint(0, len(special_char)-1)])
print(result)
# Přeskupení znaků v heslu
# translator = ""
# for index in range(0,10):
#     random_index_1 = random.randint(0,len(result)-1)
#     random_index_2 = random.randint(0,len(result)-1)
#     translator = result[random_index_2]
#     result[random_index_2] = result[random_index_1]
#     result[random_index_1] = translator

# Funkce shuffle
random.shuffle(result)
print(result)
# Převod listu na string
result_password = ""
for one_character in result:
    result_password += one_character
print(result_password)