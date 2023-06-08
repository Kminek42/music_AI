import random

def get_set(data, size):
    l = len(data)
    start = random.randint(0, l - 2 * size)
    return [data[start : start + size], data[start + size : start + 2 * size]]
