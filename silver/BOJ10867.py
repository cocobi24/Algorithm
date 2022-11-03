# https://www.acmicpc.net/problem/10867

n = int(input())
nums = sorted(list(set((map(int, input().split())))))
print(*nums, end='')