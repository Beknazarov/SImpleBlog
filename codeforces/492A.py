n = int(input())
s = 0
i = 0
a = 0
if n < 4:
    print(1)
else:
    while a <= n:

        if a + s + i >= n:
            break
        i += 1
        s += i
        a += s

    print(i)
