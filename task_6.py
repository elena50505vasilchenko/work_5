def func_file():
    try:
        with open("text_6.txt", "r", encoding="utf-8") as file:
            dict_1 = {}
            lines = file.readlines()
            for line in lines:
                if len(line):
                    subj = line.split()
                    summa = 0
                    for hours in subj[1:]:
                        if len(hours) > 1:
                            summa += int(hours.split('(')[0])
                    dict_1[subj[0]] = summa
            print(f"\t{dict_1}\n")
    except IOError:
        print("\tОшибка!\n")


func_file()
