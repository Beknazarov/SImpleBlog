n, d = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
s = 0

a = sorted(a)

zanyat = n - m
if zanyat == 0:
    s = sum(a)
elif zanyat > 0:
    s = sum(a[:m])
else:
    # print(zanyat)
    s = zanyat * d + sum(a)
print(s)
