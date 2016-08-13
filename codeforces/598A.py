t = int(input())
n = int(input())
s = int(input())

pow2 = 1
while pow2 <= n:
    s -= pow2 * 2
    pow2 *= 2

print(pow2)
