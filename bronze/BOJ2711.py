# https://www.acmicpc.net/problem/2711

t = int(input())

for _ in range(t) :
    n, s = input().split()
    s = list(s)
    s.pop(int(n)-1)
    print(''.join(s))