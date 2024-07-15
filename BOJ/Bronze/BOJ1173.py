# https://www.acmicpc.net/problem/1173

N, m, M, T, R = map(int, input().split())
X, work, time = m, 0, 0

if m+T > M:
    print(-1)
else:
    while work != N:
        if X+T > M:
            time += 1
            X -= R
            
            if X < m:
                X = m
        else :
            X += T
            work += 1
            time += 1
    print(time)