from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.forclassmates.com/cs")
soup = BeautifulSoup(response.text, "html.parser")
# all_p = soup.find_all("span")
# print(all_p)

all_class = soup.findAll(class_="tw-h3 tw-font-normal")
print(all_class)
all_a = soup.find_all("a")

for one_a in all_a:
    print(one_a.get("href"))
