book = {
    "title": "Kámen Mudrců",
    "author": "JK Rowling",
    "year": "1997"
}

# print(book["title"])
# print("year" in book.keys())
# print("1997" in book.values())
# print(book.items())

# print(book.pop("year"))
# print(book.popitem())

book.update({"year": "1996"})
print(book)
book.update({"pages": "288"})
print(book)