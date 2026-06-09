# https://www.acmicpc.net/problem/30017

A, B = map(int, input().split())

cheese = min(B, A - 1)
patty = cheese + 1

burger_size = patty + cheese
print(burger_size)