# https://www.acmicpc.net/problem/26123

N, D = map(int, input().split())
h = sorted(map(int, input().split()))

count, top, sumit = 0, 1, h.pop()
for _ in range(D):
  while len(h) > 0:
    now = h.pop()
    if now == sumit:
      top += 1
    else:
      h.append(now)
      break
  sumit -= 1
  count += top

  if sumit == 0:
    break

print(count)