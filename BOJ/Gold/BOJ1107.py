# https://www.acmicpc.net/problem/1107

n = int(input())
m = int(input())
answer = abs(100 - n)

if m != 0:
    broken_nums = list(input().split())
else:
    broken_nums = list()

for number in range(1000001):
    for num in str(number):
        if num in broken_nums:
            break
    else:
        answer = min(answer, len(str(number)) + abs(number - n))

print(answer)