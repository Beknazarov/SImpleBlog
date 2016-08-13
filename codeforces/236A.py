n = input()
n = "".join(list(set(n)))
if len(n) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")