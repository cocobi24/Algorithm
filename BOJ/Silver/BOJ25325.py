# https://www.acmicpc.net/problem/25325

import sys
input = sys.stdin.readline

T = int(input())
student = list(map(str, input().split()))
student = {student[i]:0 for i in range(len(student))}

for _ in range(T):
  s = list(map(str, input().split()))
  for i in range(len(s)):
    student[s[i]] += 1

student = sorted(student.items(), key = lambda x: (-x[1], x[0]))
for s in student:
  print(s[0], s[1])