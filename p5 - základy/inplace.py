to_do = ["feed",
        "goout",
        "atd",
        "change",
        "wash",
        "feed",
        "goout",
        "atd",
        "change",
        "wash"
]


# to_do.sort()
# to_do.reverse()
# print(to_do[::-1])

print(list(range(100)))

pozdrav = "x".join(["ahoj", "ja", "jsem", "Martin"])
print(pozdrav)

# List unpacking

a,*rest,j = to_do

print(a)
print(rest)
print(j)