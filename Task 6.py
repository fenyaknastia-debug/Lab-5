for _ in range(3):  # три числа підряд
    n = input("Введіть число (10 ≤ n ≤ 2025): ")
    max_num = max(int(n[:i] + n[i+1:]) for i in range(len(n)))
    print("Максимальне число після видалення однієї цифри:", max_num)