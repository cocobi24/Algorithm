# https://www.acmicpc.net/problem/13909

n, i, answer = int(input()), 1, 0
while i**2 <= n :
    answer += 1
    i += 1

print(answer)