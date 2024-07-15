# https://www.acmicpc.net/problem/1149

n = int(input())
home_list = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    home_list[i][0] = min(home_list[i - 1][1], home_list[i - 1][2]) + home_list[i][0]
    home_list[i][1] = min(home_list[i - 1][0], home_list[i - 1][2]) + home_list[i][1]
    home_list[i][2] = min(home_list[i - 1][0], home_list[i - 1][1]) + home_list[i][2]

answer = min(home_list[n - 1][0], home_list[n - 1][1], home_list[n - 1][2])
print(answer)