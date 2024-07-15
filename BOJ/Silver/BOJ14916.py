# https://www.acmicpc.net/problem/14916

n = int(input())
answer = 0

while n > 0 :
    if n % 5 == 0 :
        answer += n//5
        n = 0
        break
    else :
        n = n-2
        answer += 1

print(answer if n == 0 else -1)
