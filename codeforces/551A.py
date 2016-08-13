n = int(input())
arr = list(map(int, input().split()))
ls = []
count = 1
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            count += 1

    ls.append(count)
    count = 1
res = ""
for i in ls:
    res += " " + str(i)

print(res[1:])


