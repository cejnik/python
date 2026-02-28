from bs4 import BeautifulSoup
with open ("index.html") as index:
    html_code = index.read()
soup = BeautifulSoup(html_code, "html.parser")
all_a = soup.find_all("a")
with open ("a_list.txt", mode="w") as new_file:
    for a in all_a:
        new_file.write(str(a.get("href")))
        new_file.write("\n")

