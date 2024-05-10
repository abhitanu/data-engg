import requests
from bs4 import BeautifulSoup

# Define the target URL (replace with the actual URL you want to scrape)
url = "https://www.w3schools.com/tags/"

# Send an HTTP GET request to the URL and store the response
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Check if the request was successful
if response.status_code == 200:
    # Find all product elements (replace with the appropriate class or tag for products on the target website)
  product_elements = soup.find_all('div', class_='w3-col l4 m6')  

  # Extract product data
  for product in product_elements:
    # Find the element containing the product name (replace with the appropriate tag or class)
    product_name = product.find('h3').text.strip()

    # Find the element containing the product price (replace with the appropriate tag or class)
    span_element = product.find('span', class_='learn-span')

    if span_element:
        value = span_element.text.strip()
    else:
        print("Span element not found.\n")

    # Print the extracted data
    print(f"Product Name: {product_name}")
    print(f"Product Price: {span_element}")
    print("-" * 30)  # Optional separator between products

else:
  print(f"Error: Failed to download the webpage. Status code: {response.status_code}")
