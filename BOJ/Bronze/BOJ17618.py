# https://www.acmicpc.net/problem/17618

n = int(input())
answer = 0
for i in range(1, n+1):
    total = sum([int(c) for c in str(i)])
    if i % total == 0:
        answer += 1
print(answer)