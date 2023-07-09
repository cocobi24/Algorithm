# https://www.acmicpc.net/problem/2455

ans = 0
cur = 0

for _ in range(4) :
    OUT, IN = map(int, input().split())
    prev = cur
    cur = cur + IN - OUT
    ans = max(ans, prev, cur)

print(ans)