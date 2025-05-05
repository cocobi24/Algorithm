# https://www.acmicpc.net/problem/33612

y, m = 2024, 1
p = 7 * int(input())
print(y + (p // 12), m + (p % 12))