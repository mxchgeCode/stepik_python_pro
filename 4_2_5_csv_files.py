column_number = int(input())  # Считываем номер столбца для сортировки (нумерация с 1)

with open('deniro.csv', encoding='utf-8') as f:
    # Читаем строки из файла, удаляем символ переноса строки и разбиваем по запятой
    rows = [line.rstrip('\n').split(',') for line in f]

col_index = column_number - 1  # Преобразуем номер столбца в индекс (с 0)

def is_number(s):
    # Проверяем, можно ли строку s преобразовать в число
    try:
        float(s)
        return True
    except ValueError:
        return False

# Проверяем, что все значения в выбранном столбце числовые
is_numeric_column = all(is_number(row[col_index]) for row in rows)

# Выбираем функцию сортировки в зависимости от типа столбца
if is_numeric_column:
    key_func = lambda row: float(row[col_index])  # Сортируем по числовому значению
else:
    key_func = lambda row: row[col_index]         # Сортируем лексикографически по строке

# Сортируем строки по выбранному ключу (стабильная сортировка)
sorted_rows = sorted(rows, key=key_func)

# Выводим отсортированные строки, объединяя элементы через запятую
for row in sorted_rows:
    print(','.join(row))
