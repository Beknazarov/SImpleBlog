n = int(input())
arr = list(map(int, input().split()))
s = 0
print(arr[1:n].index(max(arr[1:n])))
# while arr[0] <= max(arr[1:n]):
#     s += 1
#     idex = arr[1:n].index(max(arr[1:n]))
#     arr[idex] -= 1
#     arr[0] += 1
#
# print(s)
