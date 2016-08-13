n = int(input())
res = dict()
for i in range(n):
    a = input()
    if a in res.keys():
        res[a] += 1
        print(a + str(res[a]))
    else:
        res[a] = 0
        print("OK")
