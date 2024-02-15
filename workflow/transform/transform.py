def transform_baseprice(price):
    """
    Transform the base price into an integer.
    If there is a range price, it would be use the lower price

    :param price:
    :return: converted_price
    """

    split_price = price.split(" ")
    if len(split_price) > 1:
        clean_price = "".join(s for s in split_price[0] if s.isdigit() or s == ',')
        f_clean_price = float(clean_price.replace(",", '.'))

        if 'jt' in split_price[0]:
            converted_price = int(f_clean_price * 1000000)
            return converted_price
        if 'rb' in split_price[0]:
            converted_price = int(f_clean_price * 100000)
            return converted_price
    else:
        converted_price = ''.join(s for s in split_price[0] if s.isdigit())
        return converted_price


def transform_discprice(price):
    """
    Transform the price before discount into an integer

    :param price:
    :return: converted_price
    """
    clean_price = "".join(s for s in price if s.isdigit() or s == ',')
    f_clean_price = float(clean_price.replace(",", '.'))
    if 'jt' in price:
        converted_price = int(f_clean_price * 1000000)
        return converted_price
    elif 'rb' in price:
        converted_price = int(f_clean_price * 100000)
        return converted_price
    return int(f_clean_price)



def transform_discount(discount):
    """
    Transform the discount into an integer

    :param discount:
    :return: converted_discount
    """
    converted_discount = float(discount.replace("%", ""))
    return converted_discount


def transform_cashback(cashback):
    """
    Transform the cashback into an integer

    :param cashback:
    :return: converted cashback
    """
    clean_cashback = "".join(c for c in cashback if c.isdigit() or c == ',')
    f_clean_cashback = float(clean_cashback.replace(",", '.'))
    converted_cashback = int(f_clean_cashback * 1000)
    return converted_cashback


def transform_sold(item_sold):
    """
    Transform the item_sold into an integer.
    Item sold with "+" will be rounded to the nearest

    :param item_sold:
    :return: converted_item
    """
    clean_item = item_sold.split(' ')
    if 'rb' in clean_item[0]:
        converted_item = "".join(i for i in clean_item[0] if i.isdigit())
        return int(converted_item) * 1000
    else:
        if clean_item[0].endswith('+'):
            converted_item = int(clean_item[0].replace("+", ""))
            return converted_item
        else:
            converted_item = int(clean_item[0])
            return converted_item
