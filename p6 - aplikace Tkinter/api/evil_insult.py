import requests
from tkinter import *

window = Tk()
window.minsize(400, 400)
window.resizable(False, False)
window.title("Insults")
window.config(bg="#042940")





# Funkce
def insult():
    user_language = dropdown_lang.get()
    my_parameters = {
    "lang": user_language,
    "type": "json"
    }
    response = requests.get("https://evilinsult.com/generate_insult.php?", params=my_parameters)
    response.raise_for_status()
    data = response.json()
    insult_label.config(text=data["insult"])

# Dropdown
dropdown_lang = StringVar(window)
dropdown_lang.set("en")
dropdown_lang_options = OptionMenu(window,dropdown_lang, "en", "es", "fr", "cs" )
dropdown_lang_options.config(bg="#005C53", fg="#D6D58E",font=("Helvetica", 12, "bold"))
dropdown_lang_options.pack(pady=10)

# Insult button
insult_button = Button(text="Uraž mě!", command=insult, bg="#9FC131", font=("Helvetica", 12, "bold"),borderwidth=3)
insult_button.pack(pady=10)

insult_label = Label(wraplength=250, bg="#042940", fg="#D6D58E", font=("Helvetica", 12, "bold"))
insult_label.pack()

window.mainloop()