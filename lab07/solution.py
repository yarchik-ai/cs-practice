import numpy as np
def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    values = np.array(values)
    values.reshape(values.size // width, width)
    return list(values)

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    matrix = np.array(matrix)
    return list(matrix[rows, columns])

def column_means(matrix: list[list[float]]) -> list[float]:
    matrix = np.array(matrix)
    return list(matrix.mean(axis=0).round(decimals=6))
def column_range(matrix: list[list[float]], column: int) -> float:
    matrix = np.array(matrix)
    return round(matrix[column].max() - matrix[column].min(),6)

