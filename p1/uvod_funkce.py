def greeting ():
    print("Ahoj")
    print("Já jsem Martin")
    print("Nashledanou")

def greet_name (name, surname, location):
    print(f"Ahoj, já jsem {name} {surname} z {location}")

greet_name("Martin", "Chejn", "Pardubice")
greet_name("Kristýna", "Pitelová", "Brno")

# Keyword arguments
greet_name(location="Pardubice", surname="Chejn", name="Martin")