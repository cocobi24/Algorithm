# https://www.acmicpc.net/problem/32978

n = int(input())
ingredient = set(input().split())
used = set(input().split())
ans = ingredient - used
print(*ans)