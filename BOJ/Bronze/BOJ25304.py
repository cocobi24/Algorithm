# https://www.acmicpc.net/submit/25304

sum = int(input())
n = int(input())
answer = 0

for i in range(n) :
    item = input().split()
    answer += int(item[0]) * int(item[1])

print("Yes") if sum == answer else print("No")