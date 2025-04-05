

# Імпортуємо модуль datetime
from datetime import datetime
#Оголошуємо функцію get_days_from_today, яка приймає один параметр date
def get_days_from_today(date):
    # перетворює вхідний рядок на об'єкт datetime, якщо він відповідає заданому формату
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        # Отримаемо поточну дату.
        today = datetime.today().date()
        #Обчислюємо різницю
        delta = today - given_date
        return delta.days
    # повідомлення про неправильний формат
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат: РРРР-ММ-ДД"

# Приклад використання функції
print(get_days_from_today("2022-02-24"))
print(get_days_from_today("24-02-2022")) # Помилка