# Dictionary

it_dictionary = {
    "String": "Text",
    "Integer": "Celé číslo",
    "Float": "Desetinné číslo",
    "Boolean": "Pravda nebo nepravda"
}

print(it_dictionary["Boolean"])

it_dictionary_2 = {
    0: "Text",
    1: "Celé číslo",
    2: "Desetinné číslo",
    3: "Pravda nebo nepravda"
}

print(it_dictionary_2)
# Přidání hodnot
it_dictionary_2[4] = "Uložení váce hodnot"

print(it_dictionary_2)
# Nastavení prázného dictionary
empty_dictionary = {}
# Vyprázdění dictionary
# it_dictionary_2 = {}
# print(it_dictionary_2)

# Měnění hodnot v dictionary
it_dictionary_2[1] = "Textová hodnota"
print(it_dictionary_2)