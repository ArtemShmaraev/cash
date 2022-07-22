f = open("26_2.txt")  # открытие файла
n, r = map(int, f.readline().split())
s = []
for i in range(n):
    s.append(int(f.readline()))  # append - добавление в список
s.sort(reverse=True)  # сортировка от большего к меньшему

s = s[:n // 3]  # треть лучших результатов (претенденты на призерство)
p = s[0]  # лучший результат
k = 0  # количество призеров
for i in range(len(s)):
    if p - s[i] < 10 and s[i] > (r / 2):  # если разница иеньше 10 и результат выше половины
        k += 1
        p = s[i]
print(k, p)

# 7 275



