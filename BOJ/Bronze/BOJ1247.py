# https://www.acmicpc.net/problem/1247

nums = []

while True :
    try :
        count = int(input())
        sum = 0

        for i in range(count) :
            n = int(input())
            sum += n
        nums.append(sum)
    except EOFError :
        break

for i in nums :
    if i == 0 :
        print(0)
    elif i > 0 :
        print("+")
    else :
        print("-")