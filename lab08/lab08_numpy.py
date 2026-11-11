import numpy as np
# Задание 1
hours = np.arange(0,22,3)
line = np.linspace(0,1,5)
zeros = np.zeros(6, dtype = int)
unknown_table = np.full((2,3), -1)
identity = np.eye(3)
print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

# Задание 2
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])

# Задание 3  Выведите: форму, число измерений и число элементов; значение из второй строки и третьего столбца; первую строку; последний столбец; первые две строки без первого столбца; центральный фрагмент 2×2 — строки с индексами 0 и 1, столбцы с индексами 1 и 2.
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape)
print("Количество измерений:", temperatures.ndim)
print("Количество элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:", temperatures[:2, 1:])
central = temperatures[:2, 1:3]
print("Центральный фрагмент:\n", central)

# Задание 4 Получите и выведите: первые три строки; последние две строки; первые два столбца; фрагмент из строк с индексами 1–3 и столбцов 2–4; угловой блок 2×2 в правом нижнем углу. После каждого фрагмента выведите его shape. Используйте только обычные срезы.
matrix = np.arange(1, 26).reshape(5, 5)
print("Исходная матрица:\n", matrix)

fragment1 = matrix[:3, :]
print("Первые три строки:\n", fragment1)
print("Форма:", fragment1.shape)

fragment2 = matrix[-2:, :]
print("Последние две строки:\n", fragment2)
print("Форма:", fragment2.shape)

fragment3 = matrix[:, :2]
print("Первые два столбца:\n", fragment3)
print("Форма:", fragment3.shape)

fragment4 = matrix[1:4, 2:5]
print("Фрагмент строк 1-3 и столбцов 2-4:\n", fragment4)
print("Форма:", fragment4.shape)

fragment5 = matrix[-2:, -2:]
print("Правый нижний блок 2x2:\n", fragment5)
print("Форма:", fragment5.shape)

# Задание 5


vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("\nПример изменения вектора:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("Пример изменения матрицы:\n", small_matrix)

# Создаем копию, чтобы не изменять исходный массив hours
changed_hours = hours.copy()

changed_hours[2:5] = 99
changed_hours[::2] = -1

print("\nЗадание 5")
print("Измененный hours:", changed_hours)
print("Исходный hours:", hours)

# copy() создает независимую копию массива.
# Без copy() изменения changed_hours затронули бы исходный hours.

changed_matrix = matrix.copy()

changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("Измененная матрица:\n", changed_matrix)
print("Исходная матрица:\n", matrix)

# Задание 6

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("\nЗадание 6")
print("numbers:\n", numbers)
print("Форма numbers:", numbers.shape)

print("table:\n", table)
print("Форма table:", table.shape)

print("transposed:\n", transposed)
print("Форма transposed:", transposed.shape)

# reshape(3, 4) работает, потому что 3 * 4 = 12,
# то есть количество элементов не меняется.
# reshape(5, 3) вызовет ошибку, потому что 5 * 3 = 15,
# а в исходном массиве только 12 элементов.

