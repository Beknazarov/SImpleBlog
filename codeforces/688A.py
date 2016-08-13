n, d = map(int, input().split())
cur = 0
ans = 0
for i in range(d):
    s = input()
    if s == '1' * n:
        cur = 0
    else:
        cur += 1
    ans = max(ans, cur)
    print(ans)
print(ans)
