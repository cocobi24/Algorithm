# https://www.acmicpc.net/problem/2444

n = int(input())
for i in range(n, 0, -1):
    print(' ' * (i-1), '*' * (n-i+1), '*' * (n-i), sep="")
for i in range(n, 0, -1):
    print(' ' * (n-i+1), '*' * (i-1), '*' * (i-2), sep="")