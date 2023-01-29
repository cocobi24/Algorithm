# https://www.acmicpc.net/problem/20044

n = int(input())
nums = sorted(list(map(int, input().split())))
l = len(nums)
teams = []

for i in range(l//2) :
    teams.append(nums[i] + nums[l-i-1])

print(min(teams))