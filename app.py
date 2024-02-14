import argparse
from workflow import index

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Web scrapping tokopedia for product information')
    parser.add_argument('--product_name', type=str, help='input product name', required=True)

    args = parser.parse_args()

    index.main(args)
