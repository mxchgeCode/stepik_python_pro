import csv
import re


def sort_key(class_name):
    # Ключ сортировки для классов вида "<номер>-<буква>"
    # Разбиваем на номер и букву, номер преобразуем в int для числовой сортировки
    match = re.match(r'(\d+)-(.+)', class_name)
    if match:
        number = int(match.group(1))
        letter = match.group(2)
        return (number, letter)
    else:
        # Если формат не совпадает, возвращаем класс без изменений (на всякий случай)
        return (float('inf'), class_name)


with open('student_counts.csv', encoding='utf-8') as f_in:
    reader = csv.reader(f_in)
    headers = next(reader)  # читаем заголовок

    # Первый столбец - 'year', остальные - классы
    year_col = headers[0]
    classes = headers[1:]

    # Сортируем классы по номеру и букве
    sorted_classes = sorted(classes, key=sort_key)

    # Формируем новый порядок столбцов: 'year' + отсортированные классы
    new_headers = [year_col] + sorted_classes

    # Читаем все данные в память
    data = list(reader)

with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(new_headers)

    for row in data:
        year = row[0]
        # Создаем словарь для быстрого доступа к значениям по классу
        row_dict = dict(zip(headers, row))
        # Формируем новую строку в нужном порядке столбцов
        new_row = [year] + [row_dict[cls] for cls in sorted_classes]
        writer.writerow(new_row)
