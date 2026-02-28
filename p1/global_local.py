# student = "Harry"

# def test():
#     student = "David"
#     return student

# result = test()
# print(result)

# # BlockScope
# number1 = 5
# if number1 < 10:
#     new_number = 30

# print(new_number)

# Globální proměnná
def test1():
    global my_name
    my_name = "Harry"
    print(my_name)

test1()
print(my_name)