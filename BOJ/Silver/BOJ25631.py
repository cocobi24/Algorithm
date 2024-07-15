# https://www.acmicpc.net/problem/25631

from collections import Counter
n = int(input())
mart = list(map(int, input().split()))
print(max(Counter(mart).values()))