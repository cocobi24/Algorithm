# https://www.acmicpc.net/problem/26340

N = int(input())

for _ in range(N):
  a, b, c = map(int, input().split())
  nums = sorted([a, b])

  for i in range(c):
    nums[1] //= 2
    nums.sort()

  print(f"Data set: {a} {b} {c}")
  print(nums[1], nums[0])
  print()