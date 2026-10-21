def count_items(values: list) -> dict:
    counts = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts

def unique_sorted(values: list) -> list:
    s = set()
    for value in values:
        if value not in s:
            s.add(value)
    return sorted(list(s))

def common(first: list, second: list) -> list:
    s = []
    for value in first:
        if value  in second:
            s.append(value)
    return sorted(s)

def only_in_first(first: list, second: list) -> list:
    s = []
    for values in first:
        if values not in second:
            s.append(values)
    return sorted(s)