year = int(input("Napiš rok, který bys chtěl vědět, zda je přestupný? \n"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Rok je přestupný")
else:
    print("Není přestupný")