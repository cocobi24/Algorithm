# https://www.acmicpc.net/problem/15059

A = list(map(int, input().split()))
R = list(map(int, input().split()))

ans = 0
for i in range(len(A)):
    lack = R[i] - A[i]
    ans += lack if lack > 0 else 0
print(ans)