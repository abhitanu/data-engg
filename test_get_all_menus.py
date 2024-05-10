import requests
from bs4 import BeautifulSoup

def get_chickfila_menu():
    # Define the target URL (replace with the actual URL you want to scrape)
    url = "https://www.chick-fil-a.com/menu"

    # Send an HTTP GET request to the URL and store the response
    response = requests.get(url)

    print(response.status_code)

    # Check if the request was successful
    if response.status_code != 200:
        exit
        # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all product elements (replace with the appropriate class or tag for products on the target website)
    product_elements = soup.find_all('div', class_='location-menu-card item')
    num_products = len(product_elements)
    #print(f"Number of products: {num_products}")

    print("-" * 30)  # Optional separator between products
    print(f"Chick-A-Fila Menu: {num_products}")
    print("-" * 30)  # Optional separator between products
    # Extract product data
    for product in product_elements:
        # Find the element containing the product name (replace with the appropriate tag or class)

        span_element = product.find('span', class_='item-title')

        if span_element:
            sandwich_name = span_element.text.strip()
        else:
            print("Span element with class 'item-title' not found.")

        span_calorie = product.find('span', string=lambda text: text and "Cal" in text)

        if span_calorie:
            calorie = span_calorie.text.strip()
            print(f"Item: {sandwich_name}, Calorie: {calorie}")
        else:
            print("Span element with class 'item-title' not found.")

def get_mcDonald_menu():
    url = "https://www.mcdonalds.com/us/en-us/full-menu/chicken-and-fish-sandwiches.html"

    # Send an HTTP GET request to the URL and store the response
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    product_elements = soup.find_all('div', class_='cmp-category__item-details') 

    num_products = len(product_elements)

    # Check if the request was successful
    if response.status_code == 200:
        # Find all product elements (replace with the appropriate class or tag for products on the target website)
        product_elements = soup.find_all('div', class_='cmp-category__item-details')
    
        print("-" * 30)  # Optional separator between products
        print(f"McDonalds Menu: {num_products}")
        print("-" * 30)  # Optional separator between products
        # Extract product data
        for product in product_elements:
        # Find the element containing the product name (replace with the appropriate tag or class)
            div_element = product.find('div', class_='cmp-category__item-name')

            if div_element:
                sandwich_name = div_element.text.strip()
                print(f"Item: {sandwich_name}")
            else:
                print("Span element with class 'item-title' not found.")

def get_dunkin_menu():
    url = "https://www.dunkindonuts.com/en/menu/sandwiches-and-more"

    # Send an HTTP GET request to the URL and store the response
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    product_elements = soup.find_all('a', class_='u-cta u-cta--primary')
    num_products = len(product_elements)

    print("-" * 30)  # Optional separator between products
    print(f"Dunkin Menu: {num_products}")
    print("-" * 30)  # Optional separator between products
    # Extract product data

    for product in product_elements:
        # Find the element containing the product name (replace with the appropriate tag or class)

        #anchor_element = product.find('div', class_='cta-group    ')
        sandwich_name = product.text.strip()

        if sandwich_name:
            print(f"Item: {sandwich_name}")
        else:
            print("Anchor element with class 'cta-group    ' not found.")

get_chickfila_menu()
get_mcDonald_menu()
get_dunkin_menu()