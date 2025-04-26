import csv

with open('prices.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    headers = next(reader)  # заголовки: Магазин;Творог;Гречка;...
    products = headers[1:]  # список продуктов

    # Переменные для хранения минимальной цены, продукта и магазина
    min_price = None
    min_product = None
    min_store = None

    for row in reader:
        store = row[0]
        prices = row[1:]

        for product, price_str in zip(products, prices):
            price = int(price_str)

            if (min_price is None or
                price < min_price or
                (price == min_price and product < min_product) or
                (price == min_price and product == min_product and store < min_store)):
                min_price = price
                min_product = product
                min_store = store

print(f"{min_product}: {min_store}")
