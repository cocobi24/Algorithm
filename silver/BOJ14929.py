# https://www.acmicpc.net/problem/14929

n = int(input())
x = list(map(int, input().split()))
total, answer = 0, 0

for i in range(n-1):
    total += x[i]
    answer += x[i+1] * total

print(answer)