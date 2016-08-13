n = int(input())
count = 0
for i in range(n):
    oper = input()
    if oper == '++X' or oper == 'X++':
        count += 1
    else:
        count -= 1

print(count)
