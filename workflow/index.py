import requests
from bs4 import BeautifulSoup

from workflow.transform import transform


def get_html(product_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
    r = requests.get(f'https://www.tokopedia.com/search?st=&q={product_name}', headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    return soup


def main(params):
    product = params.product_name
    soup = get_html(product)

    images = soup.find_all('img', class_='css-1q90pod')
    for image in images:
        src = image['src']

    products_name = soup.find_all('div', class_='prd_link-product-name')
    for product_name in products_name:
        product_name = product_name.string

    base_prices = soup.find_all('div', class_='prd_link-product-price')
    for base_price in base_prices:
        base_price = base_price.string
        transform.transform_baseprice(base_price)

    discounts = soup.find_all('div', class_='prd_badge-product-discount')
    for discount in discounts:
        discount = discount.string
        transform.transform_discount(discount)

    prices_after_discounts = soup.find_all('div', class_="prd_label-product-slash-price")
    for price in prices_after_discounts:
        price = price.string
        transform.transform_discprice(price)

    price_bef_discounts = soup.find_all('div', class_='prd_label-product-slash-price')
    for price_bef_discount in price_bef_discounts:
        price_bef_discount = price_bef_discount.string

    cashbacks = soup.find_all('div', class_='prd_label-product-price')
    for cashback in cashbacks:
        cashback = cashback.string
        transform.transform_cashback(cashback)

    toko_addresses = soup.find_all('span', class_='prd_link-shop-loc')
    for toko_address in toko_addresses:
        toko_address = toko_address.string

    toko_names = soup.find_all('span', class_='prd_link-shop-name')
    for toko_name in toko_names:
        toko_name = toko_name.string

    ratings = soup.find_all('span', class_='prd_rating-average-text')
    for rating in ratings:
        rating = float(rating.string)

    items_solds = soup.find_all('span', class_='prd_label-integrity')
    for item_sold in items_solds:
        item_sold = item_sold.string
        transform.transform_sold(item_sold)
