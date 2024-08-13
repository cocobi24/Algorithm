# https://www.acmicpc.net/problem/15969

_ = int(input())
nums = list(map(int, input().split()))
print(max(nums) - min(nums))