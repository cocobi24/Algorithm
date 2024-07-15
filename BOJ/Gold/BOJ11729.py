# https://www.acmicpc.net/problem/11729

n = int(input())
answer = []

def move_hanoi(n, start, end):
  if n == 0:
    return
  move_hanoi(n-1, start, 6-start-end)
  answer.append((start, end))
  move_hanoi(n-1, 6-start-end, end)

move_hanoi(n, 1, 3)
print(2**n - 1)
for start, end in answer:
  print(start, end)