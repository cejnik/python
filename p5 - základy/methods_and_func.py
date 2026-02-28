# # Funkce
# my_name = "Martin"
# print(len(my_name))
# # Metoda
# print(my_name.upper())

user_name = input("Zadejte své uživatelské jméno: ")
password = input("Zadejte své heslo: ")

print(f"Vaše jméno je {user_name} a heslo {'*' * len(password)} a délka je {len(password)}")