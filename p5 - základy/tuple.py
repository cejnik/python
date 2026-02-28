first_tuple = (0,1,2,3,2,5,6)

# nelze přeukládat
# print(3 in first_tuple)

# colors = {
#     "red": (255,0,0),
#     "green": (0,255,0),
#     "blue": (0,0,255)
# }

# print(colors["red"])


# print(first_tuple.count(2))
print(first_tuple.index(2))

x,y,*others = first_tuple

print(x)
print(y)
print(others)