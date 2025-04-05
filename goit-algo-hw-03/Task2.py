import random


def get_numbers_ticket(min, max, quantity):
    # Перевірка типів
    if not all(isinstance(x, int) for x in [min, max, quantity]):
        return "Помилка: всі вхідні значення мають бути цілими числами."

    # Перевірка, що min > max
    if min > max:
        return "Помилка: min не може бути більшим за max."

    # Перевірка, що кількість чисел не перевищує кількість доступних значень
    if quantity > (max - min + 1):
        return "Помилка: неможливо вибрати стільки унікальних чисел у заданому діапазоні."

    # Перевірка на додатні значення
    if quantity <= 0 or min < 0 or max < 0:
        return "Помилка: значення мають бути додатними цілими числами."

    # Генерація та сортування чисел
    numbers = sorted(random.sample(range(min, max + 1), quantity))
    return numbers

print(get_numbers_ticket(1, 49, 6))

