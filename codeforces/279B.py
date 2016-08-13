n, t = map(int, input().split())
a = list(map(int, input().split()))
summa = 0
count = 0
i = 0
if len(a) == 1 and t < a[0]:
    count = 0
elif len(a) == 1 and (t == a[0] or t - a[0] >= 0):
    count = 1
else:
    while True:
        if i == n:
            break
        elif summa + a[i] == t:
            count += 1
            break
        elif summa + a[i] < t and i < n:
            count += 1
            summa += a[i]
            i += 1
        elif summa + a[i] > t and i < n:
            i += 1


print(count)
# 10 15
# 10 9 1 1 5 10 5 3 7 2

# 6 10
# 2 3 4 2 1 1
