# https://www.acmicpc.net/problem/9286

n = int(input())
for i in range(n):
  m = int(input())
  grade = [int(input())+1 for _ in range(m)]
  grade = list(filter(lambda x: 0 < x <= 6, grade))
  print(f"Case {i+1}:")
  if len(grade) > 0:
    for g in grade:
      print(g)