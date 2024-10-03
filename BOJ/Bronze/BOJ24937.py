# https://www.acmicpc.net/problem/24937

s = "SciComLove"
l = len(s)
n = int(input())
idx = n % l
print(s[idx::]+s[:idx])