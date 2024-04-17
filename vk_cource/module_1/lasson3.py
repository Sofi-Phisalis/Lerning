a1 = int(input())
a2 = int(input())
flag = True

while True:
    b3 = input()
    if not b3:
        break
    else:
        if a1 <= int(b3) <= a2:
            continue
        else:
            flag = False

print(flag)