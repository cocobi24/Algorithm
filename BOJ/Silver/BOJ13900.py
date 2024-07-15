# https://www.acmicpc.net/problem/13900

n = int(input())
nums = list(map(int, input().split()))
total, answer = sum(nums), 0

for num in nums :
    total -= num
    answer += total * num

print(answer)