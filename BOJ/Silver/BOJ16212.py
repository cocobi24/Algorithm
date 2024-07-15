# https://www.acmicpc.net/problem/16212

t = int(input())
nums = sorted(list(map(int, input().split())))
print(*nums)