# https://www.acmicpc.net/problem/1059

L = int(input())
nums = sorted(map(int,input().split()))
n = int(input())
cnt = 0
start, last = 0, 1001
if n in nums:
	print(0)
else:
  for i in range(L):
    if nums[i] > n:
      last = nums[i]
      if i-1 > -1:
        start = nums[i-1]
      break

  for i in range(start+1, last):
    for j in range(i+1, last):
      if i <= n <= j:
        cnt += 1

  print(cnt)