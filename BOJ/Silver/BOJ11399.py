# https://www.acmicpc.net/problem/11399

n = int(input())
times = sorted(list(map(int, input().split())))
answer = 0
for time in times :
    answer += time * n
    n -= 1
print(answer, end='')