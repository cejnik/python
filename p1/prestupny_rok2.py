def leap(user_year): 
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days(user_year, user_month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_result = leap(user_year)
    if leap_result == True and user_month == 2:
        return 29
    else:
        return days_in_month[user_month - 1]

year = int(input("Jaký rok chcete zkontrolovat? "))
month = int(input("Zadejte měsíc číslem: "))
result = days(year, month)
print(f"Počet dnů ve zvoleném měsíci je: {result}")