# https://www.acmicpc.net/problem/27332

A = int(input())
B = int(input())
days = B * 7 + A
print('0' if days > 30 else '1')