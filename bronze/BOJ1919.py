# https://www.acmicpc.net/problem/1919

a = list(input().rstrip())
b = list(input().rstrip())

a_set = { _:0 for _ in set(a) }
b_set = { _:0 for _ in set(b) }
for _ in a:
  a_set[_] += 1
for _ in b:
  b_set[_] += 1

for _ in set(a):
  if _ in b_set:
    a_set[_] = abs(a_set[_] - b_set[_])
    b_set[_] = 0

answer = sum(a_set.values()) + sum(b_set.values())
print(answer)