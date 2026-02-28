try:
    with open("chyba.txt", mode= "w") as my_file:
        print(my_file.read())
except FileNotFoundError as not_found_error:
    print("Soubor nenalezen. Zkontrolujte název souboru")
except IOError as in_out_error:
    print("IO chyba")


