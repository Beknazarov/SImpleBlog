a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = int(input())
suma = sum(a)
sumb = sum(b)
res = 0
if suma >= 5:
    res = int(suma / 5)
if suma % 5 != 0:
    res += 1
if sumb >= 10:
    res += int(sumb / 10)
if sumb % 10 != 0:
    res += 1
if res <= n:
    print("YES")
else:
    print("NO")
