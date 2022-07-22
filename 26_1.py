f = open("26_1.txt")  # открытие файла
n = int(f.readline())
s = []
for i in range(n):
    m, d = map(int, f.readline().split())
    s.append([d, m, 0])  # цена, готовность, потрачено на район

gorod = 0  # готовность всех раонов
for i in range(n):
    d, m, k = s[i][0], s[i][1], s[i][2]
    if m < 50:  # если готовность меньше 50
        k += (50 - m) * d   # достраваем район до 50
        m = 50
    gorod += m
    s[i][0], s[i][1], s[i][2] = d, m, k
s.sort()   # сортируем список
for i in range(n):
    d, m, k = s[i][0], s[i][1], s[i][2]
    if (gorod + (100 - m)) / n <= 70:   # если город можно достроить до 100, не пробив отметку готовности в 70%
        k += (100 - m) * d
        gorod += 100 - m
        m = 100
        s[i][0], s[i][1], s[i][2] = d, m, k
    else:
        ost = (n * 70) - gorod
        k += d * ost
        m += ost
        gorod += ost
        s[i][0], s[i][1], s[i][2] = d, m, k
        break
summa = 0
mx = 0
# подсчитываем сумму и максимум
for i in range(n):
    summa += s[i][2]
    mx = max(mx, s[i][2])
print(summa, mx)




#8933 975


