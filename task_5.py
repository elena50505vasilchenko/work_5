def create_file_with_numbers(n):
    global i
    file = open(f"text_5.txt", "w", encoding="utf-8")
    summa = 0
    for i in n:
        file.write(f"{int(i)}\n")
        summa = summa + int(i)
    return summa


print(create_file_with_numbers(input().split()))
