from datetime import datetime, date, timedelta

# 1. Перетворення рядка у дату
def string_to_date(date_str):
    return datetime.strptime(date_str, "%Y.%m.%d").date()

# 2. Форматування дати назад у рядок
def date_to_string(date_obj):
    return date_obj.strftime("%Y.%m.%d")

# 3. Підготовка списку користувачів (перетворення рядків дат у date-об'єкти)
def prepare_user_list(users):
    for user in users:
        user["birthday"] = string_to_date(user["birthday"])
    return users

# 4. Знаходження наступного потрібного дня тижня
def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

# 5. Перенесення на понеділок, якщо день народження — вихідний
def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:  # 5 = субота, 6 = неділя
        return find_next_weekday(birthday, 0)  # 0 = понеділок
    return birthday

# 6. Головна функція для отримання списку привітань
def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    end_date = today + timedelta(days=days)

    for user in users:
        # День народження в цьому році
        birthday_this_year = user["birthday"].replace(year=today.year)

        # Якщо день народження вже минув — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Різниця в днях між сьогоднішнім днем та днем народження
        delta_days = (birthday_this_year - today).days

        # Якщо день народження в діапазоні [0; days]
        if 0 <= delta_days <= days:
            congratulation_date = adjust_for_weekend(birthday_this_year)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": date_to_string(congratulation_date)
            })

    return upcoming_birthdays
