a = input()
n = set(list(a))
var = int("".join(n))
if var == 74 or var == 47 or var == 7 or var == 4:
    print("YES")
else:
    b = int(a)
    if b % 4 == 0 or b % 7 == 0 or b % 47 == 0 or b % 74 ==0:
        print("YES")
    else:
        print("NO")
