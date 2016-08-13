n = input()
if len(n) > 1:
    if n[1:].isupper() and n[0].islower():
        print(n[0].upper() + n[1:].lower())
    elif n.isupper():
        print(n.lower())
    else:
        print(n)
else:
    if n.islower():
        print(n.upper())
    else:
        print(n.lower())