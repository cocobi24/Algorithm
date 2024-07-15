# https://www.acmicpc.net/problem/1629

a, b, c = map(int, input().split())

def solution(a, b, c):
    if b == 1:
        return a % c
    else :
        temp = solution(a, b // 2, c) ** 2
        if b % 2 == 0:
            return temp % c
        else:
            return (temp * a) % c

answer = solution(a, b, c)
print(answer)