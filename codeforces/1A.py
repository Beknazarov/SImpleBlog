import math

n, m, a = map(int, input().split())
res = math.ceil(n / a) * math.ceil(m / a)
print(res)

# n = int(input())



# if n <= 1:
#     print(0)
# else:
#     print(n - 1)
