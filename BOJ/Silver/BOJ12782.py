# https://www.acmicpc.net/problem/12782

T = int(input())
for _ in range(T):
    N, M = input().split()
    err = 0
    for i in range(len(N)):
        if N[i] != M[i]:
            err += 1
    N0 = N.count('0')
    M0 = M.count('0')
    cnt = max(N0, M0) - min(N0, M0)
    print(cnt + (err - cnt)//2)