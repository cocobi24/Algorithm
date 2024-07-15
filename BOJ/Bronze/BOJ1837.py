# https://www.acmicpc.net/problem/1837

P, K = map(int, input().split())
answer = ["GOOD"]

for i in range(2, K):
    if P % i == 0:
        answer = ["BAD", i]
        break

print(*answer)