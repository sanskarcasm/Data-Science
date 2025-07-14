import requests
from bs4 import BeautifulSoup
import csv
import re

with open("books.csv", "w", newline="", encoding="utf-8-sig") as f:

    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])

    for page in range(1, 51):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(url)
        response.encoding = 'utf-8'

        if response.status_code != 200:
            print(f"Failed to retrieve page {page}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")
        if not books:
            print(f"No books found on page {page}. Stopping.")
            break

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            # Force price to be £ + numbers
            price = re.sub(r'[^\d.,]', '', price)
            price = "£" + price
            writer.writerow([title, price])
            print(f"Saved: {title} | {price}")

print("Scraping complete! Data saved to books.csv")

