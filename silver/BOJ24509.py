# https://www.acmicpc.net/problem/24509

import sys
input = sys.stdin.readline

n = int(input())
answer = ''
students = [list(map(int, input().split())) for _ in range(n)]
for i in range(4):
  students.sort(key=lambda x: (x[i+1], -x[0]))
  answer += str(students[-1][0]) + ' '
  students.pop()
print(answer.rstrip())