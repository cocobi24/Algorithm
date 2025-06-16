# https://www.acmicpc.net/problem/30822

n = int(input())
s = input().rstrip()
target = ['u', 'o', 's', 'p', 'c']
ans = 9999
for t in target:
    ans = min(ans, s.count(t))
print(ans)