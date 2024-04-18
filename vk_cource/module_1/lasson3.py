a1 = int(input())
a2 = int(input())
flag = True

while True:
    b3 = input()
    if not b3:
        break
    if not a1 <= int(b3) <= a2:
        flag = False

print(flag)