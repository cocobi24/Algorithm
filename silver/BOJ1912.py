# https://www.acmicpc.net/problem/1912

n = int(input())
nums = list(map(int, input().split()))
answer = [nums[0]]

for i in range(1, len(nums)):
    answer.append(max(answer[i-1]+nums[i], nums[i]))
print(max(answer))