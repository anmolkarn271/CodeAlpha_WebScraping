import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all product blocks
products = soup.find_all("article", class_="product_pod")

# Data list
data = []

for product in products:
    # Title
    title = product.h3.a["title"]

    # Product Link
    link = url + product.h3.a["href"]

    # Price
    price = product.find("p", class_="price_color").text

    # Availability
    availability = product.find("p", class_="instock availability").text.strip()

    # Rating (class name like "star-rating Three")
    rating = product.p["class"][1]

    # Add to list
    data.append({
        "Title": title,
        "Price": price,
        "Availability": availability,
        "Rating": rating,
        "Link": link
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save CSV
df.to_csv("products.csv", index=False)

print("Scraping Completed! File Saved as products.csv")

