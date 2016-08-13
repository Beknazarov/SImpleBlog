n = input()
count0 = 0
count1 = 0
status = False
if len(n) > 7:
    for i in n:
        if i == str(0):
            count1 = 0
            count0 += 1
            status = True
            if count0 == 7:
                status = False
                print("YES")
                break

        elif i == str(1):
            count0 = 0
            count1 += 1
            status = True
            if count1 == 7:
                status = False
                print("YES")
                break
    if status:
        print("NO")


else:
    print("NO")
