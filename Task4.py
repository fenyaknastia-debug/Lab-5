a = list(map(int, input("Введіть список чисел: ").split()))
k = int(input("Введіть індекс елемента, який потрібно видалити: "))

for i in range(k, len(a) - 1):
    a[i] = a[i + 1]

a.pop()

print("Результат:", *a)