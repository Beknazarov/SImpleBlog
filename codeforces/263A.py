n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))
n3 = list(map(int, input().split()))
n4 = list(map(int, input().split()))
n5 = list(map(int, input().split()))

if sum(n1) > 0:
    index1 = n1.index(1)
    print(abs(3 - (index1 + 1)) + 2)
elif sum(n5) > 0:
    index5 = n5.index(1)
    print(abs(3 - (index5 + 1)) + 2)
elif sum(n2) > 0:
    index2 = n2.index(1)
    print(abs(3 - (index2 + 1)) + 1)
elif sum(n4) > 0:
    index4 = n4.index(1)
    print(abs(3 - (index4 + 1)) + 1)
else:
    index3 = n3.index(1)
    print(abs(3 - (index3 + 1)))
