# Slicing
to_do = ["feed",
        "goout",
        "atd",
        "change",
        "wash"
]

print(to_do[0:4])

# list je mutable
to_do[0] = "new_task"
print(to_do)

# Kopírovnáí
# nepřeukldat

to_do3 = to_do[:]
to_do3[0] = "něco"
print(to_do)
print(to_do3)
