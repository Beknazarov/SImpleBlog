n = int(input())
result = set()
a = [input() for i in range(n)][::-1]

for j in range(len(a)):
    if not a[j] in result:
        print(a[j])
        result.add(a[j])
