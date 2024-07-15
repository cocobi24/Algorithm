# https://www.acmicpc.net/problem/10992

n, p = int(input()), -1
for i in range(n, 0, -1):
    if i == n :
        print(' ' * (i - 1) + '*')
    elif i == 1 :
        print('*' + '*' * p + '*')
    else:
        print(' ' * (i-1) + '*' + ' ' * p + '*')
    p += 2