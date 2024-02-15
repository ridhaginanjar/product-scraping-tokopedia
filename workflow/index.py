import requests
from bs4 import BeautifulSoup

from workflow.transform import transform
from workflow.export import export


def get_html(product_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
    r = requests.get(f'https://www.tokopedia.com/search?st=&q={product_name}', headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    return soup


def main(params):
    product = params.product_name
    soup = get_html(product)

    products = []

    product_elements = soup.find_all('div', class_='prd_container-card')
    for product_element in product_elements:
        data = {}

        # Extract Image
        try:
            images = product_element.find('img', class_='css-1q90pod')['src']
            data['images'] = images
        except:
            data['images'] = None

        # Extract product_name
        try:
            products_name = product_element.find('div', class_='prd_link-product-name').string
            data['product_name'] = products_name
        except:
            data['product_name'] = None

        # Extract base_price
        try:
            base_prices = product_element.find('div', class_='prd_link-product-price').string
            converted_baseprice = transform.transform_baseprice(base_prices)
            data['base_price'] = converted_baseprice
        except:
            data['base_price'] = None

        # Extract discount
        try:
            discount = product_element.find('div', class_='prd_badge-product-discount').string
            converted_discount = transform.transform_discount(discount)
            data['discount'] = converted_discount
        except:
            data['discount'] = None

        # Extract prices_after_discount
        try:
            prices_after_discounts = product_element.find('div', class_="prd_label-product-slash-price").string
            converted_discprice = transform.transform_discprice(prices_after_discounts)
            data['price_before_discount'] = converted_discprice
        except:
            data['price_before_discount'] = None

        # Extract cashback
        try:
            cashback = product_element.find('div', class_='prd_label-product-price').string
            converted_cashback = transform.transform_cashback(cashback)
            data['cashback'] = converted_cashback
        except:
            data['cashback'] = None

        # Extract toko_address
        try:
            toko_address = product_element.find('span', class_='prd_link-shop-loc').string
            data['toko_address'] = toko_address
        except:
            data['toko_address'] = None

        # Extract toko_name
        try:
            toko_name = product_element.find('span', class_='prd_link-shop-name').string
            data['toko_name'] = toko_name
        except:
            data['toko_name'] = None

        # Extract rating
        try:
            rating = soup.find('span', class_='prd_rating-average-text').string
            data['ratings'] = float(rating)
        except:
            data['ratings'] = None

        # Extract item_sold
        try:
            item_sold = product_element.find('span', class_='prd_label-integrity').string
            converted_items_solds = transform.transform_sold(item_sold)
            data['items_sold'] = converted_items_solds
        except:
            data['items_sold'] = None

        products.append(data)

    export.export(products)