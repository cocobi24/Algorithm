# https://www.acmicpc.net/problem/1026

n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())))
answer = 0
while True :
    if len(a) == 0 :
        break;
    aa = a.pop()
    bb = b.pop()
    answer += aa*bb
print(answer, end='')