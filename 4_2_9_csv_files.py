import csv

# Списки для хранения имён выживших мальчиков и девочек младше 18 лет
boys = []
girls = []

with open('titanic.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)  # пропускаем заголовок

    for row in reader:
        survived = row[0]  # 0 или 1 - выжил ли пассажир
        name = row[1]  # имя пассажира
        sex = row[2]  # пол пассажира
        age = row[3]  # возраст пассажира (строка)

        # Проверяем, что пассажир выжил и возраст указан и меньше 18
        if survived == '1' and age and float(age) < 18:
            if sex == 'male':
                boys.append(name)
            elif sex == 'female':
                girls.append(name)

# Сначала выводим имена мальчиков, затем девочек, сохраняя исходный порядок
for name in boys:
    print(name)
for name in girls:
    print(name)
