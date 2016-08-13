n = int(input())
if n % 2 != 0:
    print(0)
else:
    if n % 4 == 0:
        print(int((n / 4) - 1))
    else:
        print(int(n / 4))
