import requests
from bs4 import BeautifulSoup

# Define the target URL (replace with the actual URL you want to scrape)
url = "https://www.chick-fil-a.com/menu"

# Send an HTTP GET request to the URL and store the response
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
  # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

# Find all product elements (replace with the appropriate class or tag for products on the target website)
#product_elements = soup.find_all('div', class_='location-menu-card item')  
product_elements = soup.find_all('div', class_='location-menu-card item')
num_products = len(product_elements)
print(f"Number of products: {num_products}")

# Extract product data
for product in product_elements:
    # Find the element containing the product name (replace with the appropriate tag or class)

    #span_element = product.find('span', class_='item-title').text.strip()
    span_element = product.find('span', class_='item-title')

    if span_element:
        sandwich_name = span_element.text.strip()
        #print(f"Sandwich Name: {sandwich_name}")
    else:
        print("Span element with class 'item-title' not found.")

    span_calorie = product.find('span', text=lambda text: text and "Cal" in text)

    if span_calorie:
        calorie = span_calorie.text.strip()
        #print(f"Calories: {calorie}")
        print(f"Sandwich Name: {sandwich_name}, Calorie: {calorie}")
    else:
        print("Span element with class 'item-title' not found.")