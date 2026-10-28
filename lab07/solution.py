import numpy as np
def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    values = np.array(values)
    values = values.reshape(values.size // width, width)
    return values.tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    matrix = np.array(matrix)
    return matrix[np.ix_(rows, columns)].tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    if len(matrix) == 0:
        return []
    matrix = np.array(matrix)
    return matrix.mean(axis=0).round(decimals=6).tolist()

def column_range(matrix: list[list[float]], column: int) -> float:
    if len(matrix) == 0:
        return 0.0
    matrix = np.array(matrix)
    return round(float(matrix[:,column].max() - matrix[:,column].min()),6)

