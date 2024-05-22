# https://www.acmicpc.net/problem/14652

n, m, k = map(int, input().split())
n = k // m
m = k % m
print(n, m)