# Úkol č.1
from bs4 import BeautifulSoup
with open("info.html") as info:
    html_tags = info.read()
soup = BeautifulSoup(html_tags, "html.parser")

# # Úkol č.2
# heading1 = soup.find("h1")
# print(heading1) 
# # Úkol č.3
# heading2 = soup.find("h2")
# print(heading2)
# # Úkol č.4
# history_list = soup.find("ul")
# print(history_list)
# # Úkol č.5
# all_p = soup.find_all("p")
# print(all_p[0])
# print(all_p[1])
# # Úkol č.6
# for one_p in all_p:
#     print(one_p)
# Úkol č.7
# for one_p in all_p:
#     print(one_p.getText())
# Úkol č.8
# all_a = soup.find_all("a")
# print(all_a)
# Úkol č.9
# for one_a in all_a:
#     print(one_a)
# Úkol č. 10
# for one_a in all_a:
#     print(one_a.getText())

# for one_a in all_a:
#     print(one_a.get("href"))
all_class = soup.find(class_ = "company-name")
print(all_class)