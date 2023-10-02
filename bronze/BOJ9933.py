# https://www.acmicpc.net/problem/9933

import sys
input = sys.stdin.readline
n = int(input())

word_list = []
for _ in range(n):
  s = input().rstrip()
  l = len(s)

  if s == s[::-1] or s[::-1] in word_list:
    answer = s[l//2]
    print(l, answer)
    break
  else:
    word_list.append(s)