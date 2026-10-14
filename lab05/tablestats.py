def total_minutes(rows,kind):
    total = 0
    for row in rows:
        if row["тип"] == kind:
            total += float(row["минуты"])
    return round(total, 1)

def read_rows(lines):
    if not lines:
        return []
    headers = lines[0].strip().split(",") # заголовок
    rows = []
    for line in lines[1:]:
        line = line.strip() # убираем первые и последние пробелы, перенос строки
        if not line: # проверка на пустые строки
            continue
        line = line.split(",") # разделяем элементы по запятой и закидывает в список
        if len(line) != len(headers): # проверка на целостность строки
            continue
        row = dict(zip(headers, line)) # создание словаря
        rows.append(row)
    return rows

def count_types(rows):
    count_run = 0
    count_error = 0
    for row in rows:
        if row["тип"] == 'запуск':
            count_run += 1
        if row["тип"] == "ошибка":
            count_error += 1
    return {"запуск": count_run,"ошибка": count_error}

def to_csv(counts):
    lines = ["тип,количество"]
    for key in sorted(counts):
        lines.append(f"{key},{counts[key]}")
    return "\n".join(lines) + "\n" # объединяем строки, добавляя перенос строки




