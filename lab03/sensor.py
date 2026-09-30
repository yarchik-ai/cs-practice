porog = float(input())
cnt = int(input())
excess = 0
max_indication = None
summ = 0
Error = 0
for i in range(cnt):
    s = input()
    if s == 'error':
        Error += 1
    else:
        value = float(s)
        summ += value
        if value > porog:
            excess += 1
        if max_indication is None or value > max_indication:
            max_indication = value
cnt_record = cnt - Error
average = summ / cnt_record
print(cnt)
print(Error)
print(excess)
print(f'{max_indication:.1f}')
print(f'{average:.1f}')

















