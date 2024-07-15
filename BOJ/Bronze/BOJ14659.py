# https://www.acmicpc.net/problem/14659

N = int(input())
nums = list(map(int, input().split()))
answer, current_num, cnt = 0, 0, 0

for num in nums :
    if num > current_num :
        current_num = num
        cnt = 0
    else :
        cnt += 1
    answer = max(answer, cnt)
print(answer)