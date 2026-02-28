import tkinter

# Okno
window = tkinter.Tk()
window.title("Převod měny")
window.minsize(width=500, height=500)
window.resizable(True,True)
window.iconbitmap("money.ico.ico")
window.config(bg="grey")

# Druhé okno
window2 = tkinter.Tk()
window2.title("Moje druhé okno")
# window2.minsize(300, 350)
window2.geometry("300x400+200+250")
window2.resizable(False, False)
window2.iconbitmap("money.ico.ico")
window2.config(bg="grey")


# Label(Popisek)

greet_label = tkinter.Label(window2,text="Ahooooj", bg="red", fg="white",font=("Helvetica", 24, "italic"))
greet_label.pack(side="top")














# Hlavní cyklus - drží otevřené okno
window.mainloop()

