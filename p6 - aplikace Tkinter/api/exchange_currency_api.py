from tkinter import *
import requests
# https://marketplace.apilayer.com/account
# APIKEY = Z8aNuvyZWHDa22D87b5hv0BOyix7fNKd


def count():
    currency_from = currency_dropdown.get()
    currency_to = currency_dropdown_to.get()
    amount = float(user_input.get())
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
    payload = {}
    headers= {
    "apikey": "Z8aNuvyZWHDa22D87b5hv0BOyix7fNKd"
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    response.raise_for_status
    result = response.json()
    try:
        result_label["text"] = round(result["result"],2)
    except:
        if amount == 0:
            warning_label["text"] = "Zadejte hodnotu větší než 0!"
            result_label["text"] = ""
        else:
            print("Chyba")


# Colors
main_color = "#14085f"

window = Tk()
window.minsize(400,120)
window.resizable(False, False)
window.title("Převod měn v2.0")
window.config(bg=main_color)

# Input
user_input = Entry(width=20, font=("Helvetica",12), justify="center" )
user_input.insert(0, "0")
user_input.grid(row=0, column=0, padx=10, pady=(10,0))

# Dropdown
currency_dropdown = StringVar(window)
currency_dropdown.set("CZK")
currency_dropdown_option = OptionMenu(window, currency_dropdown, "CZK", "EUR", "USD")
currency_dropdown_option.grid(row=0, column=1, padx=10, pady=(10,0))

currency_dropdown_to = StringVar(window)
currency_dropdown_to.set("CZK")
currency_dropdown_to_option = OptionMenu(window, currency_dropdown_to, "CZK", "EUR", "USD")
currency_dropdown_to_option.grid(row=1, column=1, padx=10, pady=(10,0))

# Button
exchange = Button(text="Exchange!", font=("Helvetica",12), justify="center",  bg=main_color, fg="white", command=count)
exchange.grid(row=0, column=2, padx=10, pady=(10,0))

# Label
result_label = Label(text="", font=("Helvetica",12, "bold"), justify="center", bg=main_color, fg="white")
result_label.grid(row=1,column=0, padx=10, pady=(10,0))

# Warning label
warning_label = Label(text="", bg=main_color, fg="white", font=("Helvetica",12), justify="center" )
warning_label.grid(row=2, column=0)

window.mainloop()