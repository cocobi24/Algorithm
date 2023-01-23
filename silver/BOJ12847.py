# https://www.acmicpc.net/problem/12847

n, m = map(int, input().split())
nums = list(map(int, input().split()))

window = sum(nums[:m])
answer = window
for i in range(m, n) :
    window += nums[i] - nums[i - m]
    answer = max(answer, window)
print(answer)