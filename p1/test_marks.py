set1 = ["🤠", "🤠", "🤠"]
set2 = ["🤠", "🤠", "🤠"]
set3 = ["🤠", "🤠", "🤠"]
all_sets = [set1, set2, set3]
# print(f"{set1}\n{set2}\n{set3}\n")

position = input("Zadejte souřadnice z matice 3x3: ")
position1 = int(position[0])
position2 = int(position[1])
print(position1, position2)
all_sets[position1][position2] = "👽"
print(f"{set1}\n{set2}\n{set3}\n")

