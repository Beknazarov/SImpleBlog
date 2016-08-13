n = int(input())
arr = list(map(int, input().split()))
count = 0
maxel = arr[0]
minel = maxel
for i in range(1, len(arr)):
    if arr[i] > maxel :
        maxel = arr[i]
        count += 1
    if arr[i] < minel:
        count += 1
        minel = arr[i]

print(count)