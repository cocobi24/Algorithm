# https://www.acmicpc.net/problem/13164

n, k = map(int, input().split())
height = sorted(map(int, input().split()))
temp = []
for i in range(n-1):
  temp.append(height[i+1] - height[i])
temp.sort()
ans = sum(temp[:n-k])
print(ans)