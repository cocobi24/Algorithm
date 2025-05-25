# https://www.acmicpc.net/problem/28281

N, X = map(int, input().split())
A = list(map(int, input().split()))

min_cost = 999999999
for i in range(N-1):
    cost = A[i] + A[i+1]
    if cost < min_cost:
        min_cost = cost
print(min_cost * X)