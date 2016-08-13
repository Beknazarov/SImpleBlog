n = int(input())

arr = list(map(int, input().split()))
count1 = arr.count(1)
count2 = arr.count(2)
count3 = arr.count(3)
count4 = arr.count(4)
# res = 0
# summa = sum(arr)
# if count4:
#     res += count4
#     summa -= count4 * 4
#
# if count3 and count1 > count3:
#     res += count3
#     count1 -= count3
# elif count1 and count1 < count3:
#     res += count1
#     count3 -= count1
# if count2:
#     if count2 % 2 == 0:
#         res += count2 / 2
#     else:
#         res += (count2 - 1) / 2
#         count2 = 1
# print(res)
#
# if sum(arr) >= 4:
#
#     s = sum(arr) // 4
#
#     l = sum(arr) % 4
#     if not count1 and not count4:
#         print("YES")
#         if count2 % 2 == 0:
#             print(int(count2 / 2 + count3))
#
#         else:
#             print(int((count2 - 1) / 2 + count3 + 1))
#
#     elif l == 0:
#         print(l + s)
#     else:
#         print(s + 1)
# else:
#     print(1)
ans = count4 + count3
count1 = max(0, count1 - count3)
ans += (count2 + count2 + count1 + 3) / 4
print(int(ans))

