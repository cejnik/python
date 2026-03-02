import bcrypt
from tkinter import *
import psycopg2

# Function
    
def password_to_hash(plain_password):
    # Převod na byty
    password_bytes = plain_password.encode('utf-8')
    # Encryptování hesla na hash a vrací hash
    hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hash

def insert_bank_user(email, password):
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

def get_hash_from_database(email):
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

def login_auth(password, email):
    # Vezmu heslo z databáze, které je zahashované
    hash = get_hash_from_database(email)
    password_byte = bytes(password, encoding='utf-8')
    if hash == b'':
        print('Neplatné')
    else:
        if bcrypt.checkpw(password_byte, hash):
            print('Úspěšné přihlášení')
        else:
           print('Neplatné')