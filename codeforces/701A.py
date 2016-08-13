n = int(input())
arr = list(map(int, input().split()))
total = min(arr) + max(arr)
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if total == arr[i] + arr[j] and i != j:
            print(i + 1, j + 1)
            arr[j] = 0
            break


# R  - игра
if n % 2 == 0:
    print(2)
else:
    print(1)