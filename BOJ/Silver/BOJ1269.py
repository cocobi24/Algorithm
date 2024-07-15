# https://www.acmicpc.net/problem/1269

n, m = map(int, input().split())
x = set(list(map(int, input().split())))
y = set(list(map(int, input().split())))
answer = (x | y) - (x & y)
print (len(answer), end='')