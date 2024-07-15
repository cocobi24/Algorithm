# https://www.acmicpc.net/problem/2846

N = int(input())
nums = list(map(int, input().split()))
answer, start = 0, nums[0]

for i in range(1, N) :
    if nums[i-1] < nums[i]:
        answer = max(answer, nums[i] - start)
    else :
        start = nums[i]
print(answer)