import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movies_title = [movie.getText() for movie in movies]
movies_title.reverse()

print(movies_title)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies_title:
        file.write(f"{movie}\n")
