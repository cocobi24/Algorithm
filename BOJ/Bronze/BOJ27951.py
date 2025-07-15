# https://www.acmicpc.net/problem/27951

N = int(input())
A = list(map(int, input().split()))
U, D = list(map(int, input().split()))

reqA1 = U - A.count(1) if U - A.count(1) > 0 else 0
reqA2 = D - A.count(2) if D - A.count(2) > 0 else 0
a3 = A.count(3)

if a3 - (reqA1 + reqA2) < 0:
    print("NO")
    exit(0)

A3 = ['U'] * reqA1 + ['D'] * reqA2
print('YES')
for i in range(N):
    if A[i] == 1:
        print('U', end='')
    elif A[i] == 2:
        print('D', end='')
    else:
        print(A3.pop(), end='')