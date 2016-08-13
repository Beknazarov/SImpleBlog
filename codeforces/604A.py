a = [500, 1000, 1500, 2000, 2500]
m = list(map(int, input().split()))
w = list(map(int, input().split()))
hs, hu = map(int, input().split())
summa = 0
for i in range(len(m)):
    maxbal = max(0.3 * a[i], (1 - m[i] / 250) * a[i] - 50 * w[i])
    summa += maxbal

hs *= 100
hu *= 50

print(int(summa + hs - hu))
