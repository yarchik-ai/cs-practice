def total_minutes(rows,kind):
    total = 0
    for row in rows:
        if row["тип"] == kind:
            total += float(row["минуты"])
    return round(total, 1)

def read_rows(lines):
    headers = None
    rows = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        values = [value.strip() for value in line.split(",")]
        if headers is None:
            headers = values
            continue
        if len(values) != len(headers):
            continue
    return rows

def count_types(rows):
    counts = {}
    for row in rows:
        kind = row["тип"]
        if kind not in counts:
            counts[kind] = 0
        counts[kind] += 1
    return counts
def to_csv(counts):
    lines = ["тип,количество"]
    for key in sorted(counts):
        lines.append(f"{key},{counts[key]}")
    return "\n".join(lines) + "\n" # объединяем строки, добавляя перенос строки




