def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                parts = line.split(',')
                cat = {'id': parts[0], 'name': parts[1], 'age': parts[2]}
                cats_info.append(cat)

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []
    return cats_info


cats_info = get_cats_info("/Users/palarmous/Desktop/GoIt/goit-algo-hw-04/task_02/cats_file.txt")
print(cats_info)