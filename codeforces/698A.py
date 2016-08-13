n = int(input())
word = str(input()).lower()
alphabet = list("abcdefghijklmnopqrstuvwxyz")
result = False
if len(word) >= 26:
    for i in word:
        if i in alphabet:
            alphabet.remove(i)
            result = True
else:
    result = False
if result and len(alphabet) == 0:
    print("YES")
else:
    print("NO")
