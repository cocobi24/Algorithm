# https://www.acmicpc.net/problem/1356

n = input()
l = len(n)

isYujinsu = False
for i in range(1, l):
  front, rear = 1, 1

  for a in range(i):
    front *= int(n[a])

  for b in range(i, l):
    rear *= int(n[b])

  if front == rear :
    isYujinsu = True
    break

print("YES" if isYujinsu else "NO")