# https://www.acmicpc.net/problem/9907

num = input()
nums = list(map(int, list(num)))
weight = [2, 7, 6, 5, 4, 3, 2]
upper = ['J', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Z']

sum_value = 0
for i in range(7):
    sum_value += nums[i] * weight[i]
print(upper[sum_value % 11])