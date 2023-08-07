"""Создайте функцию генератор чисел Фибоначчи"""


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = fibonacci_generator()

# Генерация первых 10 чисел Фибоначчи
for _ in range(10):
    print(next(fibonacci))
