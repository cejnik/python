from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.forclassmates.com/cs")
soup = BeautifulSoup(response.text, "html.parser")
print(soup)

articles = soup.findAll(class_="atm-link atm-link--show-visited atm-link--styled color-primary-1 article__title")

with open("seznam.txt", mode="w", encoding="utf-8") as file:
    for one_article in articles:
        one_article_text = one_article.getText()
        one_article_link = one_article.get("href")
        if "NATO" in one_article_text:
            file.write(one_article_text)
            file.write("\n")
            file.write(one_article_link)
            file.write("\n")