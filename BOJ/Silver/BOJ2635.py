# https://www.acmicpc.net/problem/2635

n = int(input())
nums = []
counts = []

for i in range(0, n) :
    nums.append([])
    nums[i].append(n)
    nums[i].append(i+1)
    start, end = 0, 1
    num = nums[i][start]-nums[i][end]
    while num >= 0:
        nums[i].append(num)
        start += 1
        end += 1
        num = nums[i][start]-nums[i][end]
    counts.append(len(nums[i]))
idx = counts.index(max(counts))
print(len(nums[idx]))
print(*nums[idx])