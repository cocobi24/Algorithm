# https://www.acmicpc.net/problem/108833

import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
  student, apple = map(int, input().split())
  ans += apple % student
print(ans)