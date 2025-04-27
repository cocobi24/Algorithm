# https://www.acmicpc.net/problem/28110

n = int(input())
nums = sorted(map(int, input().split()))
diff_list = dict()
for i in range(n - 1):
  a, b = nums[i], nums[i+1]
  num = (a+b) // 2
  if num not in nums:
    diff_list[num] = (num, min(num-a, b-num))
ans = sorted(diff_list.values(), key=lambda x:(-x[1], x[0]))
print(-1 if len(ans) == 0 else ans[0][0])