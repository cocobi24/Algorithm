# https://www.acmicpc.net/problem/21756

n = int(input())
nums = [i for i in range(1, n+1)]

while len(nums) != 1:
    temp, i = [], 1
    for num in nums:
        if i % 2 == 0:
            temp.append(num)
        i += 1
    nums = temp
print(nums[0])