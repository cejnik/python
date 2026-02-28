from bs4 import BeautifulSoup
import requests

response = requests.get("http://www.ekospace.cz/")
web = response.text

soup = BeautifulSoup(web, "html.parser")
text_book = soup.find(name="a", class_="ucebniceMakro")
pdf = (text_book.get("href"))
url = f"http://www.ekospace.cz/{pdf}"

response2 = requests.get(url)
with open("ucebnice2.doc", mode="wb") as ucebnice:
    ucebnice.write(response2.content)