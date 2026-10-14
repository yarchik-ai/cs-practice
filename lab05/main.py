from tablestats import read_rows
def count_types1(rows):
    count_run = 0
    count_error = 0
    count_check = 0
    count_exit = 0
    for row in rows:
        if row["тип"] == 'запуск':
            count_run += 1
        if row["тип"] == "ошибка":
            count_error += 1
        if row["тип"] == "проверка":
            count_check += 1
        if row["тип"] == "выгрузка":
            count_exit += 1
    return {"запуск": count_run,"ошибка": count_error,"проверка": count_check,"выгрузка": count_exit}
with open(input(),'r',encoding="utf_8") as table:
    rows = read_rows(table.readlines())
    count = count_types1(rows)
    count_key = 0 # количество различных типов
    summ = 0  # количество прочитанных записей
    summ_error = 0 # суммарные минуты записей типа "ошибка"
    for key in count:
        summ += count[key]
        count_key += 1
    for row in rows:
        if row["тип"] == "ошибка":
            summ_error += float(row["минуты"])
print(summ)
print(count_key)
print(summ_error)

with open('summary.csv','w',encoding="utf_8") as file:
    file.write(f'{summ}\n,{count_key}\n,{summ_error}\n')
