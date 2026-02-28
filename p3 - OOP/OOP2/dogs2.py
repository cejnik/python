class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1 = Dog("Harry", 13)
dog2 = Dog("Lopata", 5)
dog3 = Dog("Lampion", 2)

list_dog = [dog1, dog2, dog3]

def oldest_dog(list_dog):
    oldest_dog_age = 0
    for one_dog in list_dog:
        if one_dog.age > oldest_dog_age:
            oldest_dog_age = one_dog.age
    return oldest_dog_age

print(oldest_dog(list_dog))


def oldest(*args):
    return max(args)

result = oldest(dog1.age, dog2.age, dog3.age)

print(f"Věk nejstaršího psa je {result}")









    