# https://www.acmicpc.net/problem/16499

n = int(input())
words = {}

for _ in range(n) :
    s = ''.join(sorted(input()))
    if s not in words :
        words[s] = 1
print(len(words))