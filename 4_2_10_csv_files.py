import csv
from datetime import datetime

# Словарь для хранения самой свежей записи для каждого email
latest_records = {}

with open('name_log.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)  # считываем заголовок

    for row in reader:
        username, email, dtime_str = row
        # Преобразуем строку с датой и временем в объект datetime для сравнения
        dtime = datetime.strptime(dtime_str, '%d/%m/%Y %H:%M')

        # Если email ещё не встречался или текущая запись свежее, обновляем словарь
        if email not in latest_records or dtime > latest_records[email][2]:
            latest_records[email] = (username, email, dtime)

# Сортируем записи по email в лексикографическом порядке
sorted_records = sorted(latest_records.values(), key=lambda x: x[1])

# Записываем результат в новый файл
with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(headers)  # записываем заголовок
    for record in sorted_records:
        # Преобразуем datetime обратно в строку нужного формата
        dtime_str = record[2].strftime('%d/%m/%Y %H:%M')
        writer.writerow([record[0], record[1], dtime_str])
