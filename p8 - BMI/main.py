from tkinter import *
import psycopg2

root = Tk()
root.title('Výpočet BMI')
root.geometry('250x250')
root.resizable(False, False)


# Labels
label_general = Label(root, text='Calculate BMI')
label_general.grid(row=0, column=1)
label_weight = Label(root, text="Insert weight: ")
label_weight.grid(row=1, column=0)
label_height = Label(root,text='Insert height: ')
label_height.grid(row=2, column=0)
label_weight_unit = Label(root, text='kg')
label_weight_unit.grid(row=1, column=3)
label_height_unit = Label(root,text='m')
label_height_unit.grid(row=2, column=3)
label_result_BMI = Label(root, text='Result: ')
label_result_BMI.grid(row=4, column=0)
label_user_result_BMI = Label(root, text='Doplnit')
label_user_result_BMI.grid(row=4, column=1)
label_user_result_BMI_text = Label(root, text='Text result: ')
label_user_result_BMI_text.grid(row=5, column=0)
label_user_result_BMI_text = Label(root, text='Doplnit')
label_user_result_BMI_text.grid(row=5, column=1)
label_count_text = Label(root, text='Users: ')
label_count_text.grid(row=6, column=0)
label_count_number = Label(root, text='Doplnit')
label_count_number.grid(row=6, column=1)


# Inputs
entry_weight = Entry(root)
entry_weight.grid(row=1, column=1)
entry_height = Entry(root)
entry_height.grid(row=2, column=1)


# Button
calculate_button = Button(root, text="Calculate")
calculate_button.grid(row=3, column=1)













root.mainloop()