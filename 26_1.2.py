f = open("26_1.txt")  # открытие файла
n = int(f.readline())
s = []
gorod = 0
for i in range(n):
    m, d = map(int, f.readline().split())
    k = 0
    if m < 50:
        k += (50 - m) * d
        m = 50
    gorod += m
    s.append([d, m, k])  # цена, готовность, потрачено на район
s.sort()
i = 0
while (gorod / n) < 70:
    if s[i][1] < 100:
        s[i][1] += 1
        s[i][2] += s[i][0]
        gorod += 1
    else:
        i += 1

summa = 0
mx = 0
# подсчитываем сумму и максимум
for i in range(n):
    summa += s[i][2]
    mx = max(mx, s[i][2])
print(summa, mx)


