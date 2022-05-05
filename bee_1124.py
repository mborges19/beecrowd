num = int(input())
while num < 2:
    num = int(input())

if (num + 1) % 2 != 0:
    print(num-1, num+2)

elif (num - 1) % 2 == 0:
    print(num-2, num+1)
