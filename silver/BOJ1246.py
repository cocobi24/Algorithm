# https://www.acmicpc.net/problem/1246

n, m = map(int, input().split())
p_list = sorted([int(input()) for _ in range(m)])
cost, income = 0, 0

for i in range(m):
    egg = min(m - i, n)

    if income < p_list[i] * egg:
        income = p_list[i] * egg
        cost = p_list[i]

print(cost, income)