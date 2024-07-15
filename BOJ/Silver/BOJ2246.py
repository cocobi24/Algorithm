# https://www.acmicpc.net/problem/2246

N = int(input())
condo_list = sorted([list(map(int ,input().split())) for _ in range(N)])
cost = 99999
answer = 0

for condo in condo_list :
    temp = condo[1]
    if temp < cost :
        cost = temp
        answer += 1
print(answer)