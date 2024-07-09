# https://www.acmicpc.net/problem/14713

import sys
input = sys.stdin.readline
n = int(input().rstrip())
s = [input().rstrip().split() for i in range(n)]
l = input().rstrip().split()

length = len(l)
for _ in range(length) :
  word = l.pop()
  for i in range(len(s)) :
    if s[i] != [] and word == s[i][-1] :
      s[i].pop()
      word = ""
      break
  if word :
    break

flag = True
for _ in s :
  if _ != [] :
    flag = False
    break

print("Possible" if l == [] and word == "" and flag else "Impossible")