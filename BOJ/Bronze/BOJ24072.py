# https://www.acmicpc.net/problem/24072

A, B, C = map(int, input().split())
is_coming = 1 if A <= C and C < B else 0
print(is_coming)