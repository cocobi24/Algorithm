# https://www.acmicpc.net/problem/4929

while True:
  root1 = list(map(int, input().split()))
  root2 = list(map(int, input().split()))
  if root1[0] == 0:
    break

  root1 = root1[1:]
  root2 = root2[1:]

  uniq = sorted(set(root1) & set(root2))
  total, s1, s2 = 0, 0, 0
  for u in uniq:
    e1 = root1.index(u)
    e2 = root2.index(u)
    sum1 = sum(root1[s1:e1])
    sum2 = sum(root2[s2:e2])
    total += max(sum1, sum2)
    s1, s2 = e1, e2

  total += max(sum(root1[s1:]), sum(root2[s2:]))
  print(total)