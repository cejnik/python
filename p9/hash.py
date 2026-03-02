import bcrypt

password = b'admin'
hash = bcrypt.hashpw(password, bcrypt.gensalt())

print(hash)