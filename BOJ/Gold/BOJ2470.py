# https://www.acmicpc.net/problem/2470

N = int(input())
nums = sorted(map(int, input().split()))

L, R = 0, N-1
total = abs(nums[L] + nums[R])
answer = [nums[L], nums[R]]
while L < R:
  lv, rv = nums[L], nums[R]
  temp = lv + rv
  if abs(temp) < total:
    total = abs(temp)
    answer = [lv, rv]

  if temp == 0:
    break
  elif temp < 0:
    L += 1
  else:
    R -=1
print(answer[0], answer[1])