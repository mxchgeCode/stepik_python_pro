import csv


def condense_csv(filename, id_name):
    # Словарь для хранения данных объектов
    # Ключ - имя объекта, значение - словарь свойств и их значений
    data = {}
    properties = []  # Список свойств (названий столбцов, кроме id_name)

    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            obj_name, prop, val = row
            if i == 0:
                # Запоминаем порядок свойств по первой строке
                properties.append(prop)
            else:
                # Если свойство новое, добавляем в список (на всякий случай)
                if prop not in properties:
                    properties.append(prop)

            # Создаем словарь для объекта, если его ещё нет
            if obj_name not in data:
                data[obj_name] = {}
            data[obj_name][prop] = val

    # Записываем результат в condensed.csv
    with open('condensed.csv', 'w', encoding='utf-8', newline='') as f_out:
        writer = csv.writer(f_out)
        # Заголовок: id_name + свойства
        writer.writerow([id_name] + properties)

        # Для каждого объекта выводим имя и значения свойств в порядке properties
        for obj_name, props in data.items():
            row = [obj_name] + [props[prop] for prop in properties]
            writer.writerow(row)
