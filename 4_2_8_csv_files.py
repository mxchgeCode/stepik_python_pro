import csv

# Создаем словарь для подсчёта общего количества точек доступа по каждому району
district_access_points = {}

# Открываем файл wifi.csv с разделителем ';'
with open('wifi.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)  # пропускаем заголовок

    for row in reader:
        district = row[1]  # название района (второй столбец)
        access_points = int(row[3])  # количество точек доступа (четвертый столбец)

        # Накапливаем количество точек доступа по району
        district_access_points[district] = district_access_points.get(district, 0) + access_points

# Сортируем районы по убыванию количества точек доступа,
# при равенстве - по названию района в лексикографическом порядке
sorted_districts = sorted(
    district_access_points.items(),
    key=lambda x: (-x[1], x[0])
)

# Выводим результат в требуемом формате
for district, count in sorted_districts:
    print(f"{district}: {count}")
