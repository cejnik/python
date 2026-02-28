height = input("Vložte výšku lidí v cm oddělené čárkou a mezerou \n")
height_list = height.split(", ")
suma = 0
for height_value in height_list:
    suma = suma + int(height_value)

average = suma / len(height_list)
print(f"Průměrná výška je {average}")