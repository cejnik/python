from tkinter import *

window = Tk()
window.title("Daily Tasks")
window.minsize(400,400)
window.resizable(False, False)
# window.iconbitmap("icon.ico")

# Styles
main_font = ("Times New Roman", 12)
main_color = "#ffac90"
main_button_color = "#f37c53"
window.config(bg=main_color)

# Frame
input_frame = Frame(window, bg=main_color)
text_frame = Frame(window, bg=main_color)
button_frame = Frame(window, bg=main_color)
input_frame.pack()
text_frame.pack()
button_frame.pack()

# Function
def quit():
    window.destroy()

def add_text():
    list_box.insert(END,input.get())
    input.delete(0,END)

def remove_text_item():
    list_box.delete(ANCHOR)

def delete_items():
    list_box.delete(0, END)

def save_tasks():
    with open ("tasks.txt", "w") as my_file:
        my_tasks = list_box.get(0, END)
        for one_task in my_tasks:
            if one_task.endswith("\n"):
                my_file.write(f"{one_task}")
            else:
                my_file.write(f"{one_task}\n")
        save_list_button.config(text="Saved", bg="#90EE90", state="disabled")
        window.after(500, lambda: save_list_button.config(text="Save List", bg=main_button_color, state="normal")) 
        #lambda je bezejmenná funkce. After si musí zavolat funkci, která je zavislá na objektu. 
        #Abych nevytvářil funkci, vytvořím si anonymní funkci lambda s odkazem na tlačítko.
        

def open_tasks():
    try:
        with open("tasks.txt", "r") as my_file:
            for one_line in my_file:
               list_box.insert(END, one_line)
               
    
    except:
        print("Chyba při nahrávání souboru tasks.txt")


# Input frame
input = Entry(input_frame, width=28, borderwidth=3, font=main_font)
input.grid(row=0,column=0, padx=5, pady=5)
add_button = Button(input_frame,text="Add item", borderwidth=2, font=main_font, bg=main_button_color, padx=10, command=add_text)
add_button.grid(row=0, column=1,padx=5, pady=5, ipadx=20)

# ScrollBar to Text Frame
text_scroll_bar = Scrollbar(text_frame)
text_scroll_bar.grid(row=0,column=1, sticky=N+S)

# Text Frame
list_box = Listbox(text_frame, height=15, width=45, borderwidth=3, font=main_font, yscrollcommand=text_scroll_bar.set)
list_box.grid(row=0,column=0)

# Connection scrollbar to textframe
text_scroll_bar.config(command=list_box.yview)


# Button Frame
remove_item_button =Button(button_frame, text = "Delete Item", borderwidth=2, font=main_font, bg=main_button_color, command=remove_text_item)
clear_list_button =Button(button_frame, text="Clear List", borderwidth=2, font=main_font, bg=main_button_color, command=delete_items)
save_list_button =Button(button_frame, text="Save List", borderwidth=2, font=main_font, bg=main_button_color, command=save_tasks)
quit_button =Button(button_frame, text="Quit", borderwidth=2, font=main_font, bg=main_button_color, command=quit)

# Button Styles
remove_item_button.grid(row=0,column=0,padx=5, pady=5, ipadx=8.75)
clear_list_button.grid(row=0,column=1,padx=5, pady=5, ipadx=8.75)
save_list_button.grid(row=0,column=2,padx=5, pady=5, ipadx=8.75)
quit_button.grid(row=0,column=3,padx=5, pady=5, ipadx=8.75)

# Loading of tasks
open_tasks()

# Main Cycle
window.mainloop()