n = input()
if len(n) > 1:
    if n[0].islower():
        print(n[0].upper() + n[1:])
    else:
        print(n)
else:
    if n.islower():
        print(n.upper())
    else:
        print(n)
