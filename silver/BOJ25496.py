# https://www.acmicpc.net/problem/25496

P, N = map(int, input().split())
A = sorted(map(int, input().split()))
answer = 0

for a in A :
    if P < 200 :
        P += a
        answer += 1

print(answer)