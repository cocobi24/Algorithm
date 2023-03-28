# https://www.acmicpc.net/problem/2437

n = int(input())
weight_list = sorted(list(map(int, input().split())))

target = 1
for weight in weight_list:
    if target < weight:
        break
    target += weight
print(target)