# https://www.acmicpc.net/problem/26933

N = int(input())

cost = 0
for _ in range(N):
    H, B, K = map(int, input().split())
    req = (B - H) * K
    cost += req if req > 0 else 0
print(cost)