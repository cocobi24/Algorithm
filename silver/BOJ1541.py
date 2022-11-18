# https://www.acmicpc.net/problem/1541

nums = input().split('-')
answer = 0

for num in nums[0].split("+") :
    answer += int(num)

for num in nums[1:] :
    for n in num.split("+") :
        answer -= int(n)

print(answer)