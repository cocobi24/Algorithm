# https://www.acmicpc.net/problem/26005

n = int(input())
leaf, x = [0, 2], 3
for i in range(2, 502):
  leaf.append(x)
  leaf.append(x)
  x += 2
print(sum(leaf[:n]))