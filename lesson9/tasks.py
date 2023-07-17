import csv
import json
import random
import math
import functools

# Нахождение корней квадратного уравнения
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)
    else:
        return ("Complex roots",)

# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def generate_csv(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(random.randint(100, 1001)):
            writer.writerow([random.randint(0,100) for _ in range(3)])

# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
def from_csv_decorator(func):
    @functools.wraps(func)
    def wrapper(filename):
        results = []
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                results.append(func(a, b, c))
        return results
    return wrapper

# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.json', 'a') as f:
            json.dump({'func': func.__name__, 'args': args, 'kwargs': kwargs, 'result': result}, f)
        return result
    return wrapper