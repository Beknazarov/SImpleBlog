n = int(input())
A = [0] * 1000001
idx = 1
a = list(map(int, input().split()))
for i in a:
    A[i] += 1
    if A[i] > A[idx]:
        idx = i
print(idx)
