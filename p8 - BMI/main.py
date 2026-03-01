from tkinter import *
import psycopg2

root = Tk()
root.title('Výpočet BMI')
root.geometry('250x250')
root.resizable(False, False)

# Functions
def bmi_calc(weight, height):
    text_result = ''
    bmi = round(float(weight)/float(height)/float(height),2)
    if bmi < 18.5:
        text_result = 'underweight'
    elif bmi < 24.9:
        text_result = 'normal'
    elif bmi < 29.9:
        text_result = 'overweight'
    elif bmi < 34.9:
        text_result = 'obese'
    elif bmi >= 34.9:
        text_result = 'extreme obese'
    # Results to labels
    label_user_result_BMI['text'] = bmi
    label_user_result_BMI_text ['text'] = text_result

    insert_data(bmi, text_result)

def check_dot(number):
    number_string = str(number)
    if ',' in number_string:
        return number_string.replace(',', '.')
    return number_string

def insert_data(bmi_number, bmi_text):
    connection = psycopg2.connect(
        dbname = 'health',
        user='postgres',
        password='admin',
        host='localhost',
        port='5432'
    )
    cur = connection.cursor()
    query = '''INSERT INTO bmi(bmi_number, bmi_text) VALUES (%s, %s)'''
    cur.execute(query, (bmi_number, bmi_text))
    connection.commit()
    connection.close()

def count_all_data():
    connection = psycopg2.connect(
        dbname = 'health',
        user='postgres',
        password='admin',
        host='localhost',
        port='5432'
    )
    cur = connection.cursor()
    query = '''SELECT COUNT(bmi_id) FROM bmi'''
    cur.execute(query)
    count = cur.fetchone()
    connection.close()
    return count[0]



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
label_user_result_BMI = Label(root)
label_user_result_BMI.grid(row=4, column=1)
label_user_result_BMI_text = Label(root, text='Text result: ')
label_user_result_BMI_text.grid(row=5, column=0)
label_user_result_BMI_text = Label(root)
label_user_result_BMI_text.grid(row=5, column=1)
label_count_text = Label(root, text='Users: ')
label_count_text.grid(row=6, column=0)
label_count_number = Label(root, text=count_all_data())
label_count_number.grid(row=6, column=1)

# Inputs
entry_weight = Entry(root)
entry_weight.grid(row=1, column=1)
entry_height = Entry(root)
entry_height.grid(row=2, column=1)

# Button
calculate_button = Button(root, text="Calculate", command=lambda:bmi_calc(check_dot(entry_weight.get()), check_dot(entry_height.get())))
calculate_button.grid(row=3, column=1)

root.mainloop()