# https://www.acmicpc.net/problem/1592

n, m, l = map(int, input().split())
people = [0] * n
people[0] = 1
cnt, idx = 0, 0

while True:
  if max(people) >= m:
    break

  if people[idx] % 2 != 0:
    idx = idx + l if n > idx + l else (idx + l) - n
  else:
    idx = idx - l if idx - l >= 0 else n + (idx - l)

  people[idx] += 1
  cnt += 1

print(cnt)