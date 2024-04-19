# https://www.acmicpc.net/problem/14921

n = int(input())
values = sorted((abs(int(elem)), int(elem)) for elem in input().split())
answer, prev, max_value = [], values[0][1], 2000000001
for i in range(1, n):
  value = values[i][1]
  cur = abs(prev + value)

  if cur < max_value:
      max_value = cur
      answer = [prev, value]
  prev = value

print(sum(answer))