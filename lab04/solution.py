def winner(names:list[str],scores: list[float]):
    max_score = max(scores)
    winner = ''
    for i in range(len(scores)):
        for j in range(len(names)):
            if scores[i] == max_score:
                winner = names[i]
    return winner

def average(scores: list[float]):
    return float(f'{sum(scores) / len(scores):.2f}')

def ranking (names: list[str], scores: list[float]):
    res = []
    Names = []
    for i in range(len(names)):
        for j in range(len(scores)):
            res.append([names[i], scores[j]])
    res.sort(key=lambda x: x[1], reverse=True)
    for i in res:
        Names.append(res[i][0])
    return Names

def above_average(names: list[str], scores: list[float]):
    res = []
    Names = []
    average = sum(scores) / len(scores)
    for i in range(len(names)):
        for j in range(len(scores)):
            res.append((names[i], scores[j]))
    for i in res:
        if res[i][1] > average:
            Names.append(res[i][0])
    return Names







