i = lambda: map(int, input().split())
n, k = i()
a = list(i())
print(sum([x >= a[k - 1] and x > 0 for x in a]))
