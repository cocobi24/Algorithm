# https://www.acmicpc.net/problem/1037

n = int(input())
nums = [int(i) for i in input().split()]
nums.sort(reverse=True)
lcm = nums[0] * nums[-1]
print(lcm, end='')