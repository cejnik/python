import base64
import zlib
from tkinter import *
from tkinter import filedialog

# Functions
def upload_file():
    global select_file_path
    select_file_path = filedialog.askopenfilename()
    if select_file_path:
        file_name_label.config(text=select_file_path)
    

def compress_file():
    global select_file_path
    if select_file_path:
        try:
            with open (select_file_path, 'r') as file:
                data = file.read()
            data_bytes = bytes(data, encoding='utf-8')
            compressed_data = zlib.compress(data_bytes)
            compressed_data_base64 = base64.b64encode(compressed_data)
            decoded_data = compressed_data_base64.decode('utf-8')
            with open ('compressed.txt', 'w') as file:
                file.write(decoded_data)
        except Exception as e:
            print(f'Nastala chyba při kompresi souboru: {e}')
    else:
        print('Není vybrán soubor pro kompresi')


def decompress_file():
    global select_file_path
    if select_file_path:
        try:
            with open(select_file_path, 'r') as file:
                compressed_data_base64 = file.read()
            compressed_data = base64.b64decode(compressed_data_base64)
            decompressed_data_byte = zlib.decompress(compressed_data)
            decompressed_data = decompressed_data_byte.decode('utf-8')
            with open ('after_text.txt', 'w') as new_file:
                new_file.write(decompressed_data)
        except Exception as e:
            print(f'Nastala chyba při dekompresi souboru: {e}')
    else:
            print('Není vybrán soubor pro dekompresi')


root = Tk()
root.geometry('300x300')
root.title('Komprese a dekomprese souborů')
root.resizable(False, False)

# Labels
main_label = Label(text='Komprese a dekomprese souborů')
main_label.grid(row=0, column=1)

file_name_label = Label()
file_name_label.grid(row=2, column=1)

# Buttons
upload_button = Button(text='Vyberte soubor: ', command=upload_file)
upload_button.grid(row=1, column=1)

compress_button = Button(text='Zkomprimovat', command=compress_file)
compress_button.grid(row=3, column=1)

decompress_button = Button(text='Dekomprimovat', command=decompress_file)
decompress_button.grid(row=4, column=1)

root.mainloop()