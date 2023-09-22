# https://www.acmicpc.net/problem/13458

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = N
for a in A:
    a -= B
    if a < 1:
        continue
    answer += int(a/C) if a % C == 0 else (a//C) + 1
print(answer)