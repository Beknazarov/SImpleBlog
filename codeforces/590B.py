a = list(map(int, input().split()))
n = a[0]
m = a[1]
result = 0
if n >= m:
    result = n - m
else:
    while n != m:
        if n < m and m % 2 == 0:
            m /= 2
        else:
            m += 1
        result += 1
print(result)
