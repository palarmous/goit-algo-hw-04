def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            total = 0
            count = 0
            
            for line in lines:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
            
            average = total / count if count != 0 else 0
            
            return total, average
            
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None


result = total_salary("/Users/palarmous/Desktop/GoIt/goit-algo-hw-04/task_01/salary_file.txt")

if result is not None:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")