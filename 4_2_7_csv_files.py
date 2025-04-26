import csv

# Словарь для подсчёта количества пользователей по доменам
domain_counts = {}

with open('data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # пропускаем заголовок

    for row in reader:
        email = row[2]
        domain = email.split('@')[1]  # получаем домен из email
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

# Сортируем по количеству (возрастание), при равенстве - по домену (лексикографически)
sorted_domains = sorted(domain_counts.items(), key=lambda x: (x[1], x[0]))

# Записываем результат в новый CSV файл
with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(['domain', 'count'])  # заголовок
    writer.writerows(sorted_domains)


