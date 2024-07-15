# https://www.acmicpc.net/problem/1292

a, b = map(int, input().split())
nums = []
num = 0

while True :
    num += 1
    for i in range(num) :
        nums.append(num)

    if len(nums) > 1000 :
        break

answer = sum(nums[a-1:b])
print(answer)