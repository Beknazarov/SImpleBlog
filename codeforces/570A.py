n, m = map(int, input().split())
a = [0] * 10001

for i in range(m):
    s = list(map(int, input().split()))
    index = s.index(max(s)) + 1
    a[index] += 1

resindex = a.index(max(a))
print(resindex)
