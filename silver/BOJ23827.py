# https://www.acmicpc.net/problem/23827

N = int(input())
list_A = list(map(int, input().split()))
total = sum(list_A)
answer = 0

for a in list_A :
    total -= a
    answer += a * total
    answer %= 1000000007
print(answer)