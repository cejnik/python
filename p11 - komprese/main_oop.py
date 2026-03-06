from tkinter import *
import base64
import zlib
from tkinter import filedialog

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x300')
        self.root.resizable(False, False)
        self.root.title('Komprese a dekomprese')

        self.select_file_path = None
        self.create_widgets()

    def create_widgets(self):
        # Labels
        main_label = Label(text='Komprese a dekomprese souborů')
        main_label.grid(row=0, column=1)

        self.path_label = Label()
        self.path_label.grid(row=1, column=2)
        
        # Buttons
        add_file_button = Button(text='Nahrát soubor: ', command=self.upload_button)
        add_file_button.grid(row=1, column=1)

        compression_button = Button(text='Komprese', command=self.compress_file)
        compression_button.grid(row=2, column=1)

        decopression_button = Button(text='Dekomprese', command=self.decompress_file)
        decopression_button.grid(row=3, column=1)
    
    def upload_button(self):
        self.select_file_path = filedialog.askopenfilename()
        if self.select_file_path:
            self.path_label.config(text=self.select_file_path)

    def compress_file(self):

        if not self.select_file_path:
            print('Není vybraný soubor')
            return

        try:
            with open(self.select_file_path, 'r') as file:
                data = file.read()
        
            data_bytes = bytes(data, encoding='utf-8')
            compress_data = zlib.compress(data_bytes)
            compress_data_base64 = base64.b64encode(compress_data).decode('utf-8')
            with open('compressed_data.txt', 'w') as new_file:
                new_file.write(compress_data_base64)
        except Exception as e:
            print(f'Nastala chyba při kompresi souboru: {e}')
    
    def decompress_file(self):
        if not self.select_file_path:
            print('Není vybraný soubor')
            return

        try:
            with open('compressed_data.txt', 'r') as old_file:
                    data = old_file.read()
            compress_data = base64.b64decode(data)
            decompress_bytes = zlib.decompress(compress_data)
            decompress_data = decompress_bytes.decode('utf-8')
            with open('decompress_data.txt', 'w') as new_file:
                new_file.write(decompress_data)
        except Exception as e:
            print(f'Nastala chyba při dekompresi: {e}')


window = Tk()
app = App(window)
window.mainloop()