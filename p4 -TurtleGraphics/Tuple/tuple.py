my_tuple = (1,5,6)
# my_tuple[0] = 12
# Tuple nelze měnit, tuple object does not support item assignment!!!

# Tuple to List

tuple_to_list = []

# Složitější
for tuple in my_tuple:
    tuple_new = tuple
    tuple_to_list.append(tuple_new)

# Jednodušší
tuple_to_list2 = list(my_tuple)

print(tuple_to_list)
print(tuple_to_list2)


