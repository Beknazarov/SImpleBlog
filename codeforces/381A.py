n = int(input())
a = list(map(int, input().split()))

serej = 0
dima = 0
i = 0
j = len(a) - 1
k = 2
while i <= j:
    if a[i] > a[j]:
        if k % 2 == 0:
            serej += a[i]
        else:
            dima += a[i]
        k += 1
        i += 1
    else:
        if k % 2 == 0:
            serej += a[j]
        else:
            dima += a[j]
        k += 1
        j -= 1
print(serej, dima)
