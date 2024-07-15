# https://www.acmicpc.net/problem/1822

na, nb = map(int, input().split())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
answer = sorted(a - b)
cnt = len(answer)
print(cnt)
print(*(answer), end='')