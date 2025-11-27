# https://www.acmicpc.net/problem/14175

M, N, K = map(int, input().split())

ans = []
for i in range(M):
    row = list(input().rstrip())
    temp = []
    for r in row:
        temp.append(r * K)

    for _ in range(K):
        ans.append(temp)

for i in range(M * K):
    print(*ans[i], sep='')