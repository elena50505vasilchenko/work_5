file = open("file_2.txt", "r", encoding="utf-8")
c = 0
for i in file:
    words = i.split()
    c += 1
    print(f"Количество слов в {c} строке - {len(words)}")
print(f"Количество строк - {c}")

file.close()
