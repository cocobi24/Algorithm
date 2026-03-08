# https://www.acmicpc.net/problem/3578

h = int(input())

if h == 0:
    print(1)
elif h == 1:
    print(0)
else:
    pascal = ''
    if h % 2 != 0:
        pascal = '4'
        h -= 1
    pascal += '8' * (h // 2)
    print(pascal)