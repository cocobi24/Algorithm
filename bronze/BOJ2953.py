# https://www.acmicpc.net/problem/2953

max_value = 0
idx = 0

for i in range(1, 6) :
    max_num = sum(list(map(int, input().split())))
    if max_num > max_value :
        max_value = max_num
        idx = i

print(idx, max_value)