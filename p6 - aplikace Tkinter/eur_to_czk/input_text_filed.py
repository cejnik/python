from tkinter import *

window = Tk()
window.title("převod měn")
window.minsize(500,500)
window.resizable(False, False)

label_1 = Label(text="Lorem Ipsum....", font=("Helvetica", 20, "bold"))
label_1.pack()

# Tlačítko
def change_text():
    label_1["text"]=text_field.get("1.0", END)
    # input_1.delete(0, END)

    


button_1 = Button(text="Click me", command=change_text)
button_1.pack()

# Input
input_1 = Entry(width=50)
input_1.focus()
input_1.insert(0,"Ahoj")
input_1.pack()
# input_1.get()

# Textové pole
text_field = Text(width=40, height=10)
text_field.pack()
text_field.focus()
text_field.get("1.0", END)


window.mainloop()