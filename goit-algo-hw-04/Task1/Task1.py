def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                try:
                    name, salary_str = line.strip().split(',')
                    salary = float(salary_str)
                    total += salary
                    count += 1
                except ValueError:
                    print(f"Помилка обробки рядка: {line.strip()}")
            if count == 0:
                return 0, 0
            average = total / count
            return total, average
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
