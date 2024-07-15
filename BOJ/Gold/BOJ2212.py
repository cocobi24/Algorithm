# https://www.acmicpc.net/problem/2212

n = int(input())
k = int(input())

lamp = sorted(map(int, input().split()))
interval = []
for i in range(n-1):
  interval.append(lamp[i+1] - lamp[i])
interval.sort()
ans = sum(interval[:n-k])
print(ans)