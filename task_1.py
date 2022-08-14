file = open("file_1.txt", "w", encoding="utf-8")
text_1 = input("Введите текст: \n")
for i in text_1:
    file.writelines(f"{text_1}\n")
    text_1 = input("Введите текст: \n")
    if not text_1:
        break

file.close()
