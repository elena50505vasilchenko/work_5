def func_file():
    num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    text = []
    try:
        with open('text_4.txt', 'r+', encoding="utf-8") as file:
            with open('new_text_4.txt', 'r+', encoding="utf-8") as new_file:
                c = file.readlines()
                for i in c:
                    i = i.split(' ', 1)
                    text.append(num[i[0]] + ' ' + i[1])
                new_file.writelines(text)
    except FileNotFoundError:
        return 'Файл не найден.'


func_file()
