import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('text_7.txt', 'r', encoding="utf-8") as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Средняя прибыль - {prof_aver:.2f}')
    else:
        print(f'Все фирмы в убытке')
    pr = {'Cредняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль компаний - {profit}')
with open('text_7.json', 'w', encoding="utf-8") as file_js:

    json.dump(profit, file_js, ensure_ascii=False, indent=4)



