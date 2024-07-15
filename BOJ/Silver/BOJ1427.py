# https://www.acmicpc.net/problem/1427

n = list(map(int, input()))
n.sort(reverse=True)
n = ''.join(map(str, n))
print(n)