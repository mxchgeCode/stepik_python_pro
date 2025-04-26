column_number = int(input())  # Номер столбца (с 1)
with open('deniro.csv', encoding='utf-8') as f:
    rows = [line.rstrip('\n').split(',') for line in f]

col_index = column_number - 1

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

is_numeric_column = all(is_number(row[col_index]) for row in rows)

if is_numeric_column:
    key_func = lambda row: float(row[col_index])
else:
    key_func = lambda row: row[col_index]

sorted_rows = sorted(rows, key=key_func)

for row in sorted_rows:
    print(','.join(row))
