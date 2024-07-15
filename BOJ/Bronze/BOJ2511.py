# https://www.acmicpc.net/problem/2511

A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = [0, 0]
player, winner = ['A', 'B'], 'D'
for i in range(10):
  if A[i] > B[i]:
    res[0] += 3
    winner = 'A'
  elif B[i] > A[i]:
    res[1] += 3
    winner = 'B'
  else:
    res[0] +=1
    res[1] += 1

print(res[0], res[1])
print(player[res.index(max(res))] if res[0] != res[1] else winner)