import numpy as np
def make_table(rows: int, columns: int) -> list[list[int]]:
    return np.arange(rows * columns).reshape(rows, columns).tolist()

def rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int) -> list[list[float]]:
    return np.array(matrix)[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int, value: float) -> list[list[float]]:
    result = np.array(matrix).copy()
    result[row_start:row_stop, column_start:column_stop] = value
    return result.tolist()

def matrix_vector_product(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return np.array(matrix) @ np.array(vector).tolist()

def matrix_multiply(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    return (np.array(left) @ np.array(right)).tolist()

def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    return np.array(matrix).T.tolist()

def solve_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return np.linalg.solve(matrix,vector).tolist()

def tensor_channel_mean(tensor: list) -> list:
    return np.array(tensor).mean(axis=-1).tolist()

def point_distance(first: list[float], second: list[float]) -> float:
    return np.linalg.norm(np.array(second) - np.array(first))
