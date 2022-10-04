def choose_command():
    """Для выполнения предложены три команды:
    1. Вывести иерархию команд;
    2. Вывести сводный отчёт по департаментам;
    3. Сохранить сводный отчёт по департаментам.
    """
    number = int(input('Введите номер команды, которую нужно запустить: '))
    if not 1 <= number <= 3:
        print('Введен неверный номер команды.')
    else:
        data = preprocessing()
        if number == 1:
            command_1(data)
        elif number == 2:
            command_2_2(
                command_2_1(data)
            )
        elif number == 3:
            command_3(
                command_2_1(data)
            )


def preprocessing():
    """Данная функция предобрабатывает датасет с данными"""
    with open('Corp_Summary.csv', 'r', encoding='utf8') as csv_file:
        lines = csv_file.readlines()
    data = []
    for line in lines:
        line = line.strip()
        data.append(line.split(';'))
    data.pop(0)
    return data


def command_1(data: list):
    """Данная функция выводит ответ на первый запрос:
    иерархия команд, т.е. департамент и все команды, которые входят в него
    """
    departments_and_teams = {}
    for line in data:
        department = line[1]
        team = line[2]
        if department not in departments_and_teams:
            departments_and_teams[department] = []
        if team not in departments_and_teams[department]:
            departments_and_teams[department].append(team)
    for department in departments_and_teams:
        print(f'В департамент {department} входят следующие команды: ', end='')
        print(*departments_and_teams[department], sep=', ')


def command_2_1(data: list) -> dict:
    """Данная функция сохраняет ответ на второй запрос в виде словаря:
    сводный отчёт по департаментам: название, численность,
    "вилка" зарплат в виде мин – макс, среднюю зарплату
    """
    departments_info = {}
    for line in data:
        department = line[1]
        salary = int(line[5])
        if department not in departments_info:
            departments_info[department] = {
                'staff': 0, 'min_salary': salary, 'max_salary': salary, 'total_salary': 0
            }
        departments_info[department]['staff'] += 1
        departments_info[department]['total_salary'] += salary
        if salary < departments_info[department]['min_salary']:
            departments_info[department]['min_salary'] = salary
        if salary > departments_info[department]['max_salary']:
            departments_info[department]['max_salary'] = salary
    return departments_info


def command_2_2(departments_info: dict):
    """Данная функция выводит ответ на второй запрос:
    сводный отчёт по департаментам: название, численность,
    "вилка" зарплат в виде мин – макс, среднюю зарплату
    """
    for department in departments_info:
        print(f"Информация о департаменте {department}: "
              f"Количество сотрудников: {departments_info[department]['staff']}, "
              f"Минимальная зарплата: {departments_info[department]['min_salary']}, "
              f"Минимальная зарплата: {departments_info[department]['max_salary']}, "
              f"Средняя зарплата: "
              f"{departments_info[department]['total_salary'] / departments_info[department]['staff']}")


def command_3(departments_info: dict):
    """Данная функция выводит ответ на третий запрос:
    сохраненный сводный отчёт из второго пункта в виде csv-файла
    """
    csv = ''
    for department in departments_info:
        line = ''
        line = line + department + ';'
        values = list(departments_info[department].values())
        values = [str(value) for value in values]
        line += ';'.join(values)
        line += '\n'
        csv += line
    with open('Dep_Summary.csv', 'w') as file:
        file.write(csv)


if __name__ == '__main__':
    choose_command()
