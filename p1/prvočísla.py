# Prvočísla
# číslo = 13
import math
import time
prime_number = int(input("Zadejte číslo, u kterého chcete zjistit, zda je prvočíslo: "))


def prime (prime_number):
    result = "Je to prvočíslo"
    for number in range(2,int(math.sqrt(prime_number))+1):
        if prime_number % number == 0:
            result = "Není to prvočíslo"
    print(result)

start_time = time.time()
prime(prime_number=prime_number)
end_time = time.time()
print(f"Čas trvání: {end_time - start_time:.9f} sekund")

def prime2 (prime_number):
    result = "Je to prvočíslo"
    for number in range(2,prime_number):
        if prime_number % number == 0:
            result = "Není to prvočíslo"
    print(result)

start_time = time.time()
prime2(prime_number=prime_number)
end_time = time.time()
print(f"Čas trvání: {end_time - start_time:.9f} sekund")