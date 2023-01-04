# https://www.acmicpc.net/problem/11179

n = bin(int(input()))
b = n[2:][::-1]
print(int(b, 2))