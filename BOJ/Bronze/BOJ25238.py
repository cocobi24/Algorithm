# https://www.acmicpc.net/problem/25238

a, b = map(int, input().split())
b /= 100
print(1 if 100 > a - a * b else 0)