import numpy as np
def make_hours() -> list[int]:
    return np.arange(0,22,3).tolist()

def vector_report(values: list[float]) -> dict:
    d = {}
    d['third'] = values[2]
    d['last'] = values[-1]
    d['middle'] = values[2:6]
    d['every_second'] = values[::2]
    d['reversed'] = values[::-1]
    return d

def change_vector(values: list[float]) -> list[float]:
    a = np.array(values.copy())
    a[2:4] = 99.0
    a[::2] = -1.0
    return a.tolist()

def cap_above(values: list[float], limit: float) -> list[float]:
    values = np.array(values.copy())
    values[values > limit] = limit
    return values.tolist()

def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    values = np.array(values.copy())
    values = values * (9/5) + 32
    return values.tolist()


