n = int(input())
s = 0

a = list(input())

t = list(map(int, input().split()))
ll = 0
llen = len(a)

while ll < llen:
    if a[ll] == '>':

        s += t[ll]
    elif a[ll] == '<':
        s -= t[ll]
    if s < 0 or s >= n:
        print("FINITE")
        break
    ll += 1

    if ll > n:
        print("INFINITE")
