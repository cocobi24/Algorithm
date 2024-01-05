# https://www.acmicpc.net/problem/10801

A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = [0, 0]
for i in range(10):
  if A[i] > B[i]:
    res[0] += 1
  elif B[i] > A[i]:
    res[1] += 1

winner = res.index(max(res))
player = {0:"A", 1:"B"}
print(player[winner] if res[0] != res[1] else "D")