import bcrypt
from tkinter import *
import psycopg2

# Function
def password_to_hash(plain_password):
    try:
        # Převod na byty
        password_bytes = plain_password.encode('utf-8')
        # Encryptování hesla na hash a vrací hash
        hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hash
    except Exception as e:
        print(f'Error při hashování hesla {e}')
        return None

def insert_bank_user(email, password):
    try:
        # připojení do databáze
        connection = psycopg2.connect(
            dbname = 'bank',
            user = 'postgres',
            password = 'admin',
            host='localhost',
            port = '5432'
        )
        cur = connection.cursor()
        # Query parametr v databázi
        query = '''INSERT INTO bank_user(email, password) VALUES (%s, %s)'''
        # Převedu heslo na hash
        hash = password_to_hash(password)
        # Uložím heslo a email
        cur.execute(query, (email, hash))
        connection.commit()
        connection.close()
    except psycopg2.DatabaseError as e:
        print(f'Error databáze: {e}')
    except Exception as e:
        print(f'Obecná chyba: {e}')
    else:
        print('Uživatel úspěšně přidán')

def get_hash_from_database(email):
    try:
        # Připojení do databáze
        connection = psycopg2.connect(
            dbname = 'bank',
            user = 'postgres',
            password = 'admin',
            host='localhost',
            port = '5432'
        )
        cur = connection.cursor()
        # Query parametr do databáze
        query = '''SELECT password FROM bank_user WHERE email=(%s)'''
        cur.execute(query, (email,))
        user_hash_password = cur.fetchone()
        connection.close()
        # Odeberu první dva znaky, protože jsou pokaždé stejné.
        if user_hash_password:
            return bytes.fromhex(user_hash_password[0][2:])
        else:
            return b''
    except psycopg2.DatabaseError as e:
        print(f'Error databáze: {e}')
        return b''
    except Exception as e:
        print(f'Obecná chyba: {e}')
        return b''

def login_auth(password, email):
    try:
        # Vezmu heslo z databáze, které je zahashované
        hash = get_hash_from_database(email)
        password_byte = bytes(password, encoding='utf-8')
        if hash == b'':
            log_sing_up_label['text'] = 'Neplatné'
        else:
            if bcrypt.checkpw(password_byte, hash):
                log_sing_up_label['text'] = 'Přihlášení úspěšné'
            else:
                log_sing_up_label['text'] = 'Neplatné'
        
    except Exception as e:
        log_sing_up_label['text'] = 'Došlo k chybě při ověřování'
        print(f'Chyba při ověřování uživatele: {e}')

root = Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('Registrace a přihlášení')

# Registrace
reg_label = Label(root, text='Registrace')
reg_label.grid(row=0, column=1)
email_label = Label(root, text='Email: ')
email_label.grid(row=1, column=0)

email_entry = Entry()
email_entry.grid(row=1, column=1)

password_label = Label(text='Heslo: ')
password_label.grid(row=2, column=0)

password_entry = Entry(show='*')
password_entry.grid(row=2, column=1)

reg_button = Button(root, text='Zaregistrovat se', command=lambda:insert_bank_user(email_entry.get(), password_entry.get()))
reg_button.grid(row=3, column=1)

sing_up_label = Label(text='')
sing_up_label.grid(row=4, column=1)

# Přihlášení
log_label = Label(root, text='Přihlášení')
log_label.grid(row=5, column=1)
log_email_label = Label(root, text='Email: ')
log_email_label.grid(row=6, column=0)

log_email_entry = Entry()
log_email_entry.grid(row=6, column=1)

log_password_label = Label(text='Heslo: ')
log_password_label.grid(row=7, column=0)

log_password_entry = Entry(show='*')
log_password_entry.grid(row=7, column=1)

reg_button = Button(root, text='Přihlásit se', command=lambda:login_auth(log_password_entry.get(), log_email_entry.get()))
reg_button.grid(row=8, column=1)

log_sing_up_label = Label()
log_sing_up_label.grid(row=9, column=1)

root.mainloop()