# https://www.acmicpc.net/problem/15237

N, C = map(int, input().split())
nums = list(map(int, input().split()))
sorted_set = {}

for i in range(N):
  if nums[i] not in sorted_set:
    sorted_set[nums[i]] = [i, 1, nums[i]]
  else:
    sorted_set[nums[i]][1] += 1

sorted_list = list(sorted_set.values())
sorted_list.sort(key=lambda x:(-x[1], x[0]))

l = len(sorted_list)
ans = []
for i in range(l):
  ans += ([sorted_list[i][2]] * sorted_list[i][1])
print(*ans)