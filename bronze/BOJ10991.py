# https://www.acmicpc.net/problem/10991

n = int(input())
for i in range(n, 0, -1):
    print(' ' * (i-1), '*', ' *' * (n-i), sep="")