# https://www.acmicpc.net/problem/2246

N = int(input())
condo_list = sorted([list(map(int ,input().split())) for _ in range(N)])
cost = 10001
result = 0
answer = 0
for i in condo_list:
    temp = i[1]
    if temp < cost:
        cost = temp
        answer += 1
print(answer)