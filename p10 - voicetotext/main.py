from gtts import gTTS
import os
from tkinter import *
from tkinter import ttk

# text_to_audio = open('demo.txt', 'r', encoding='utf-8').read()
# output = gTTS(text=text_to_audio, lang='en', slow=False)
# output.save('audio.mp3')

# os.system('start audio.mp3')

def translate():
    try:
        language = language_dropdown.get()
        text = text_entry.get()
        file_name = audio_entry.get()
        output = gTTS(text=text, lang=language, slow=False)
        output.save(f'{file_name}.mp3')
        os.system(f'start {file_name}.mp3')
        text_entry.delete(0, END)
        audio_entry.delete(0, END)
    except Exception as e:
        print(f'Nastala chyba {e}')

root = Tk()
root.title('Konventor z textu na řeč')
root.geometry('300x300')
root.resizable(False, False)

# Main label
main_label = Label(text='Konventor')
main_label.grid(row=0, column=1)

# Language
language_label = Label(text='Vložte jazyk: ')
language_label.grid(row=1, column=0)

language_dropdown = ttk.Combobox(
    state='readonly',
    values=['cs', 'en'],
    width=27
)
language_dropdown.grid(row=1, column=1)

# Text section
text_label = Label(text='Vložte text: ')
text_label.grid(row=2, column=0)

text_entry = Entry(width=30)
text_entry.grid(row=2, column=1)

# Audio
audio_label = Label(text='Název souboru: ')
audio_label.grid(row=3, column=0)

audio_entry = Entry(width=30)
audio_entry.grid(row=3, column=1)

# Button
translate_button = Button(text='Přeložit', command=translate)
translate_button.grid(row=4, column=1)

root.mainloop()
