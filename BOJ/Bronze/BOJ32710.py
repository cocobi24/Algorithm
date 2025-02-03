# https://www.acmicpc.net/problem/32710

gugudan = set()
for i in range(2, 10):
  for j in range(1, 10):
    gugudan.add(i * j)
    gugudan.add(i)
    gugudan.add(j)

N = int(input())
print(1 if N in gugudan else 0)