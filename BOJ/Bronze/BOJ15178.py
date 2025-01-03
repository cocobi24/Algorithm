# https://www.acmicpc.net/problem/15178

n = int(input())
for _ in range(n):
  nums = list(map(int, input().split()))
  answer = "Seems OK" if sum(nums) == 180 else "Check"
  print(*nums, answer)