# https://www.acmicpc.net/problem/10996

n = int(input())
for _ in range(n):
    for i in range(1, 3):
        if i % 2 != 0:
            for j in range(1, n+1):
                if j % 2 != 0:
                    print('*', end="")
                else:
                    print(' ', end="")
            print()
        else:
            for j in range(1, n + 1):
                if j % 2 != 0:
                    print(' ', end="")
                else:
                    print('*', end="")
            print()