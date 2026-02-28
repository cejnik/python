# formatovany_string
 

name = "martin"
age = 30

# print ("Ahoj ja jsem" + name + "a je mi " + age)
print ("Ahoj ja jsem" + name + "a je mi " + str(age))
print (f"Ahoj ja jsem {name} a je mi {age}")

# záleží na pořadí!
print ("Ahoj ja jsem {} a je mi {}".format("David", 30))
print ("Ahoj ja jsem {0} a je mi {1}".format(name, age))
print ("Ahoj ja jsem {1} a je mi {0}".format(name, age))
print ("Ahoj ja jsem {myname} a je mi {myage}".format(myname=name,myage=age))