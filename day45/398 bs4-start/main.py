from bs4 import BeautifulSoup
import lxml


with open("website.html", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.title.string)

links = soup.find_all(name="a")

for link in links:
    print(link.get_text("href"))

heading = soup.find(name="h1", id="name")
print(heading.string)

heading = soup.find(name="h1", id="name")

section_heading = soup.find(name="h3", class_="heading")
print(soup.select_one(selector=".company a"))
print(soup.select("a"))