# https://www.acmicpc.net/problem/2548

n = int(input())
nums = sorted(list(map(int, input().split())))

if (len(nums) % 2) == 0 :
    idx = (len(nums)//2)-1
else :
    idx = (len(nums)//2)

print(nums[idx])