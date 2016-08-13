a = input().lower()
b = input().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
zero = 0
for i, j in zip(a, b):
    if alphabet.index(i) > alphabet.index(j):
        print(1)
        break
    elif alphabet.index(i) < alphabet.index(j):
        print(-1)
        break
    else:
        zero += 1

if zero == len(a):
    print(0)
