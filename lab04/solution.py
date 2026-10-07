from operator import index
def winner(names:list[str],scores: list[float]):
    index = scores.index(max(scores))
    return names[index]

def average(scores: list[float]):
    return float(f'{sum(scores) / len(scores):.2f}')

def ranking (names: list[str], scores: list[float]):
    res = []
    Names = []
    for i in range(len(names)):
            res.append([names[i], scores[i]])
    res.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(res)):
        Names.append(res[i][0])
    return Names

def above_average(names: list[str], scores: list[float]):
    res = []
    Names = []
    average = sum(scores) / len(scores)
    for i in range(len(names)):
        res.append((names[i], scores[i]))
    for i in range(len(res)):
        if res[i][1] > average:
            Names.append(res[i][0])
    return Names







