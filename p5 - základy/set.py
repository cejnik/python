# Set - unikátní neseřazené hodnoty

# first_set = {1,2,2,3,8,5,5,5,5}

# # print(first_set)

# # print(first_set)


# # my_name = "martinchejn"
# # my_set = set(my_name)
# # print(my_set)

# # my_list = ["martin", "jana", "petr", "martin"]
# # result = set(my_list)
# # print(result)

# # print(first_set) #{1, 2, 3, 5, 8}
# # # print(first_set[0]) #nelze

# # for value in first_set:
# #     print(value)


# # print(3 in first_set)
# old_set = first_set.copy()
# first_set.add(100)
# print(old_set)
# print(first_set)


first_set = {1,2,3}
second_set = {2,3,4,5,6,7,8}
# first_set.remove(2) #
# print(first_set.discard(9)) # nevyhazujee chybu v případě,  že odstranuju hodnotu, která tam není
# print(first_set.difference(second_set))
# print(first_set)
# print(first_set.discard(2))

first_set.difference_update(second_set)
print(first_set)