# https://www.acmicpc.net/problem/20920

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
word_list = {}

for _ in range(n) :
    s = input().rstrip()
    if len(s) >= m :
        if s in word_list :
            word_list[s] += 1
        else :
            word_list[s] = 1

word_list = sorted(word_list.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))
for key, velue in word_list :
    print(key)