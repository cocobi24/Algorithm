# https://www.acmicpc.net/problem/16953

a,b = map(int,input().split())

answer = 1
while True:
    if a == b:
        break
    elif (b % 2 != 0 and b % 10 != 1) or (b < a):
        answer = -1
        break
    else:
        b = b // 10 if b % 10 == 1 else b // 2
        answer += 1

print(answer)