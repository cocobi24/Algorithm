# https://www.acmicpc.net/problem/14247

N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

tree = []
for i in range(N):
  tree.append([H[i], A[i]])
tree.sort(key=lambda x:(x[1], x[0]))

ans = 0
for i in range(N):
  ans += tree[i][0] + (tree[i][1] * i)
print(ans)