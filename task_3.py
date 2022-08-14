with open('text_3.txt', 'r', encoding="utf-8") as file:
    salary = []
    poor = []
    my_list = file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        salary.append(i[1])


print(f'Сотрудники, у которых оклад меньше 20000: {", ".join(poor)}. Средний оклад - {sum(map(float, salary)) / len(salary)}')
