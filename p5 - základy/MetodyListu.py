to_do = ["feed",
        "goout",
        "atd",
        "change",
        "wash",
        "feed",
        "goout",
        "atd",
        "change",
        "wash"
]

# to_do.append("Lopata")
# to_do.insert(1, "orange")
# to_do.extend(["Lopata2", "umýt okna"])
# to_do.clear()
# to_do.pop(0) #odstranění na určité pozici
# to_do.remove("wash")


# print(to_do.index("feed"))
# print("feed" in to_do) #kontrola hodnot v listu
# print(to_do.count("goout")) #kolikrát je danná hodnota v listu

to_do.sort()# nevrací žádnou hodnotu, takže nepřeukládat.

to_do2 = to_do.copy() #přeuložení a pak mužu měnit položky.

to_do2[0] = "computer"

print(to_do)
print(to_do2)
