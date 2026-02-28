height = input("Zadejte svoji výšku v cm odděleno čárkou a mezerou?")
height_list = height.split(", ")
suma = 0

for one_height in height_list:
    suma = suma + int(one_height)

average = suma / len(height_list)

print(f"Vaše průměrná výška je {average}")


    
