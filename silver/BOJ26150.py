# https://www.acmicpc.net/problem/26150

import sys
input = sys.stdin.readline

N = int(input())
str_list = []
for _ in range(N):
  S, I, D = map(str, input().rstrip().split())
  str_list.append([S, int(I), int(D)-1])
str_list.sort(key=lambda x:x[1])

solve = ''
for str in str_list:
  S, I, D = str
  solve += S[D].upper()
print(solve)