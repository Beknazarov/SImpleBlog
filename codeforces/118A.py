n = input().lower()
res = ""
for i in n:
    if i == 'a' or i == 'o' or i == 'y' or i == 'e' or i == 'u' or i == 'i':
        pass
    else:
        res += "." + i

print(res)
