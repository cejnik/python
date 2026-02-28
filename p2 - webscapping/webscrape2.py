from bs4 import BeautifulSoup
with open("index.html") as index:
    html_code = index.read()
soup = BeautifulSoup(html_code, "html.parser")
# heading = soup.find(name="h1", id="name")
# print(heading)
# heading2 = soup.find(name="h2", class_="about")
# print(heading2)

# about = soup.find_all(class_ = "about")
# print(about)
contant = soup.select_one("p a")
print(contant)
contant = soup.select("p a")
print(contant)