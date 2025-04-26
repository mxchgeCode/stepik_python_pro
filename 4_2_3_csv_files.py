with open('sales.csv', encoding='utf-8') as f:
    next(f)
    for line in f:
        name, old_price, new_price = line.strip().split(';')
        if int(new_price) < int(old_price):
            print(name)



