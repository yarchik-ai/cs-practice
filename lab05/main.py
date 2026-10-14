from lab05.tablestats import read_rows, count_types
filename = input()
with open(filename,'r',encoding="utf_8") as table:
    rows = read_rows(table.readlines())
    count = count_types(rows)
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
    file.write(f'{summ}\n,{count_key}\n,{summ_error}\n\n')
