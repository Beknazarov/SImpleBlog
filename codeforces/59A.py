n = input()
uppS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# lowS = "abcdefghijklmnopqrstuvwxyz"
low = 0
upp = 0
for i in n:
    if i in uppS:
        upp += 1
    else:
        low += 1
if low == upp or low > upp:
    print(n.lower())
else:
    print(n.upper())
