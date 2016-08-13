s = input()
res = ""
value = "hello"
j = 0
if len(value) > len(s):
    res = "NO"
else:
    for i in s:
        if res == value:
            break
        if i == value[j]:
            res += i
            j += 1
if res == value:
    print("YES")
else:
    print("NO")
