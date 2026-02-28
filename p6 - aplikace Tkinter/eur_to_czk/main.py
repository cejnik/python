from tkinter import *


window = Tk()
window.title("Převod měn")
window.minsize(500,500)
window.resizable(False, False)


# Label
# pack
# grid
# place
label1 = Label(text="Hello World 1", font=("Helvetica", 20))
label1.grid(row=0, column=0)
# label1.pack(side="bottom")
# label1.place(x=0,y=0)
label2 = Label(text="Hello World 2", font=("Helvetica", 20))
label2.grid(row=1, column=1)
# label2.place(x=200, y= 200)
# label2.pack(side="bottom")
label3 = Label(text="Hello World 3", font=("Helvetica", 20))
# label3.pack(side="bottom")
# label3.place(x=300, y=300)
label3.grid(row=3, column=3)





window.mainloop()