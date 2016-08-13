import math

n = int(input())
res = 0
a = 0

for i in range(1, n + 1):
    if n % i == 0:
        if pow(i, 2) % n == 0:
            res = i
            break
# if math.sqrt(res).is_integer():
#     a = math.sqrt(res)
# else:
#     a = res

print(int(res))
