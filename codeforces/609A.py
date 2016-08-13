n = int(input())
m = int(input())
a = []
summa = 0
# status = False
# ll = -1
# ll2 = n - 1
count = 0
for i in range(n):
    s = int(input())
    a.append(s)
a = sorted(a, reverse=True)
# a = sorted(a)
# if sum(a) <= m:
#     print(n)
# elif min(a) >= m:
#     print(1)
# else:
#     while True:
#         ll += 1
#         if ll == ll2:
#             break
#         if summa > m:
#             summa += a[ll]
#             status = False
#             print(count - 1)
#             break
#         else:
#             status = True
#             summa += a[ll]
#             if summa == m:
#                 break
#             count += 1
#     if status:
#         print(count)
for j in range(n):
    summa += a[j]
    count += 1
    if summa >= m:
        break
print(count)