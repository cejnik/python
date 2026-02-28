# def better_name (first_name, second_name):
#     first_name = first_name.capitalize()
#     second_name = second_name.capitalize()
#     return f"{first_name} {second_name}"




def better_name (first_name, second_name):
    if first_name =="" or second_name =="":
        return "Špatně jste vyplnili údaje"
    full_name = first_name + " " + second_name
    return full_name.title()

result = better_name("martin", "")
print(result)

