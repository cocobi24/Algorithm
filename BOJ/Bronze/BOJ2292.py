# https://www.acmicpc.net/problem/2292

n = int(input())
temp = 1
i = 0

while True :
    temp += (6 * i)
    if temp == n:
        print(i + 1)
        break
    elif temp > n:
        print(i+1)
        break;
    i += 1
