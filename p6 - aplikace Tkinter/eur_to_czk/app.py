from tkinter import *

window = Tk()
window.minsize(200,200)
window.title("Převod měn")
window.resizable(False, False)
window.config(bg="grey")
# window.iconbitmap("money.ico")

def transfer():
    amount_eur =float(czk_input.get())/24.58
    result_label["text"] = round(amount_eur,2)

def delete():
    result_label["text"] = 0
    czk_input.delete(0,END)


czk_label = Label(text="CZK", font=("Helvetica",20), bg="grey")
czk_label.grid(row=0, column=1)
euro_label = Label(text="EUR",font=("Helvetica",20), bg="grey")
euro_label.grid(row=1, column=1)
result_label = Label(text="0", font=("Helvetica",20), bg="grey")
result_label.grid(row=1, column=0)
info = Label(text="Aktuální kurz: 1EUR = 24.26 CZK ", font=("Helvetica",20), bg="grey")
info.place(x=0, y=150)


# input
czk_input = Entry(width=20, font=("Helvetica",20), justify="center", bg="grey")
czk_input.focus()
czk_input.grid(row=0, column=0, padx=10, pady=10)

# Button
transfer_button = Button(text="Převést",width=10, font=("Helvetica", 20), command=transfer, bg="grey")
transfer_button.grid(row=0,column=2, padx=10, pady=10)

delete_button = Button(text="Smazat", width=10, font=("Helvetica", 20), command=delete, bg="grey")
delete_button.grid(row=1, column=2, padx=10, pady=10)






window.mainloop()