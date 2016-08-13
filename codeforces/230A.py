s, n = map(int, input().split())
k = []
m = []
status = False
for i in range(n):
    a, l = map(int, input().split())
    k.append(a)
    m.append(l)

# for w, v in od.items():
#     if s <= w:
#         print("NO")
#         status = False
#         break
#
#     else:
#         status = True
#
#         s += v

#
#


if s > k[0]:
    for i in range(len(m) - 1):
        if s + m[i] > k[i + 1]:
            s += m[i]

            status = True
        else:
            status = False
            print("NO")
            break

else:
    print("NO")

if status:
    print("YES")
