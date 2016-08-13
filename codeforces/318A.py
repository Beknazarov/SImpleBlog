n, k = map(int, input().split())
s = 0
if n % 2 == 0:
    s = n / 2
else:
    s = (n + 1) / 2

if s >= k:
    print(k * 2 - 1)
else:
    print(int((k - s) * 2))
