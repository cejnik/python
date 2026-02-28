name = "testovaci"

print(name[0])

# [start:stop]
print(name[0:4])
print(name[2:5])

# [start:stop:krok]
print(name[0:8:2])

# kombinace
print(name[1:])
print(name[:6])
print(name[::1])

print(name[-1]) #í
print(name[-3]) #í

# oparně, že když jdu po zpátku, je to od -1

print(name[::-1]) #vypisovaní po zpátku
