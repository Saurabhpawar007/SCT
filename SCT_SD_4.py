import requests
from bs4 import BeautifulSoup
import csv

url = input("Enter the e-commerce product page URL: ")

headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

products = []

for item in soup.select('.product'):
    name = item.select_one('.product-name')
    price = item.select_one('.price')
    rating = item.select_one('.rating')
    products.append([
        name.text.strip() if name else 'N/A',
        price.text.strip() if price else 'N/A',
        rating.text.strip() if rating else 'N/A'
    ])

with open("products.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Price", "Rating"])
    writer.writerows(products)

print("Data saved to products.csv")