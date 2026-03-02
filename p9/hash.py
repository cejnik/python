import bcrypt

# Registrace
password = b'admin'
hash = bcrypt.hashpw(password, bcrypt.gensalt())

# Přihlášení
user_password = bytes(input('Napište své heslo: '), encoding='utf-8')

if bcrypt.checkpw(user_password, hash):
    print("Úspěšné přihlášení")
else:
    print("Špatně zadané heslo")