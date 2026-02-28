employess = ["Martin", "Harry", "Ron"]

print(employess[0])
print(employess[1])
print(employess[2])


# Mění se položky
employess[1] = "Hermiona"
print(employess)

# Přidání obsahu
employess.append("Harry")
print(employess)

# Přidání více položek
employess.extend(["Crabbe, Goyle"])

print(employess)

# Odstranění
employess.remove("Ron")
print(employess)