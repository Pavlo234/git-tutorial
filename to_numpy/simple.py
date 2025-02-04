def get_los_angeles_points(results):
    los_angeles_result = 0
    for name, score in results:
        if name.startswith('Los Angeles '):
            a = name.split()
            if len(a) == 3 and a[2][0].isupper() and a[2].isalpha() and a[2][1:].islower():
                split_score = score.split(':')

                los_angeles_result += int(split_score[0])
    return los_angeles_result     


pt = [
   ["Los Angeles dsdsds", "559:503"],
   ["Los Angels wdd", "550:511"],
   ["LosAngeles", "527:520"],
   ["Los Angeles Atomic ", "494:458"],
   ["Los Angeles", "469:460"],
   ["Los Angeles Ljiji ", "523:522"],
   ["Los Angeles Aaaaaaaaaa", "100000495:494"],
   ["Angeles Los", "399:402"],
   ["Los Angeles Pjkjz", "420:431"],
   ["Original Los Angeles", "646:658"],
   ["Original Los Angeles Guys", "382:422"],
   ["Daring Dudes from Los Angeles", "492:513"],
   ["Los Guardianos Angeles", "641:637"],
   ["Los angeles", "315:318"],
   ["losAngeles", "433:454"]
]
print(get_los_angeles_points(pt))

op = 'ood sdsd aaa'
kl = op.split()
print(kl[2])

def unite_unique(*args):
    seen = set()  # Множество для отслеживания уникальных элементов
    result = []  # Список для хранения результата
    
    for lst in args:
        for item in lst:
            if item not in seen:
                result.append(item)  # Добавляем элемент в результат, если его еще нет в множестве
                seen.add(item)  # Добавляем элемент в множество, чтобы исключить дубликаты
    
    return result
