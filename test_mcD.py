import requests
from bs4 import BeautifulSoup

# Define the target URL (replace with the actual URL you want to scrape)
url = "https://www.mcdonalds.com/us/en-us/full-menu/chicken-and-fish-sandwiches.html"

# Send an HTTP GET request to the URL and store the response
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
product_elements = soup.find_all('div', class_='cmp-category__item-details') 

# Check if the request was successful
if response.status_code == 200:
    # Find all product elements (replace with the appropriate class or tag for products on the target website)
    product_elements = soup.find_all('div', class_='cmp-category__item-details')
  
    # Extract product data
    for product in product_elements:
    # Find the element containing the product name (replace with the appropriate tag or class)
        div_element = product.find('div', class_='cmp-category__item-name')

        if div_element:
            sandwich_name = div_element.text.strip()
            print(f"Sandwich Name: {sandwich_name}")
        else:
            print("Span element with class 'item-title' not found.")

        
       