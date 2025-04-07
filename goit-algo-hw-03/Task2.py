import random


def get_numbers_ticket(min, max, quantity):
    # Перевірка типів
    if not all(isinstance(x, int) for x in [min, max, quantity]):
        return []

    # Перевірка, що min > max
    if min > max:
        return []

    # Перевірка, що кількість чисел не перевищує кількість доступних значень
    if quantity > (max - min + 1):
        return []

    # Перевірка: допустимі значення — тільки в діапазоні [1, 1000]
    if min < 1 or max > 1000:
        return []

    # Перевірка на додатні значення
    if quantity <= 0:
        return []

    # Генерація та сортування чисел
    numbers = sorted(random.sample(range(min, max + 1), quantity))
    return numbers

print(get_numbers_ticket(1000, 1200, 10)) # Перевірка на допустимі значення