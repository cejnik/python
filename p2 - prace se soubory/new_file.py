lets_continue = "yes"
while lets_continue =="yes":
    new_file = input("Jak chcete, aby se soubor jmenoval? ")
    with open(f"output/{new_file}.txt", mode ="w") as my_file:
        my_file.write(new_file)
    lets_continue = input("Chcete dále pokračovat? yes or no?")



