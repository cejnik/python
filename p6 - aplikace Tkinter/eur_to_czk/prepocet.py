# import tkinter
from tkinter import *

window =Tk()
window.minsize(width=500, height=500)
window.title("Přepočet kurzu")
window.config(bg="black")
window.iconbitmap("money.ico.ico")

currency =Label(window,text="EUR", font=("Cambira", 20, "bold"), bg="black", fg="white", relief="sunken")
currency.pack(pady=50, ipadx=50)
currency2 =Label(window, text="CZK", font=("Cambira", 20, "bold"), bg="black", fg="white",relief="sunken")
currency2.pack()


window.mainloop()