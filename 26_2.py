f = open("26_2.txt")
n, r = map(int, f.readline().split())
s = []
for i in range(n):
    s.append(int(f.readline()))
s.sort(reverse=True)  # сортировка от большего к меньшему

k = 1
mx = n // 3
mn = 2**32
for i in range(1, len(s)):
    if s[i - 1] - s[i] < 10 and s[i] > (r / 2): 
        k += 1
        mn = min(mn, s[i])
    if k == mx:
        break
print(k, mn)
print(s)

# 7 192
