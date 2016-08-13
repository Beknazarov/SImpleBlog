l, r = map(str, input().split())
resl = ""
resj = ""
# if int(l) == 3 and int(r) == 7:
#     print(20)
# else:
for i in l:
    resl += str(9 - int(i))

for j in r:
    resj += str(9 - int(j))

if int(resj) * int(r) < int(resl) * int(l):

    print(int(resj) * int(r))
else:
    print(int(resl) * int(l))
