import csv

# Чтение данных и подсчёт суммарных зарплат
company_data = {}
with open('salary_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # Пропуск заголовка
    for row in reader:
        company = row[0]
        salary = float(row[1])
        if company not in company_data:
            company_data[company] = {'total': 0, 'count': 0}
        company_data[company]['total'] += salary
        company_data[company]['count'] += 1

# Расчёт средних значений и подготовка к сортировке
sorted_companies = sorted(
    [(company, data['total']/data['count']) for company, data in company_data.items()],
    key=lambda x: (x[1], x[0])  # Сортировка по средней ЗП и названию
)

# Вывод результатов
for item in sorted_companies:
    print(item[0])
