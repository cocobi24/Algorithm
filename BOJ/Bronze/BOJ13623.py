# https://www.acmicpc.net/problem/13623

nums = list(map(int, input().split()))
winner = ['A', 'B', 'C', '*']

one = nums.count(1)
zero = nums.count(0)
if one == 1:
  idx = nums.index(1)
elif zero == 1:
  idx = nums.index(0)
else:
  idx = 3
print(winner[idx])