# https://www.acmicpc.net/problem/2703

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  crypto, pwd = list(input().rstrip()), list(input().rstrip())
  decrypt = []
  for c in crypto:
    decrypt.append(' ' if c == ' ' else pwd[ord(c) - 65])
  print(*decrypt, sep='')