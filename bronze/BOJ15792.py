# https://www.acmicpc.net/problem/15792

x, y = map(int, input().split())
print(x//y, end='')
if x % y:
    i = 0
    print('.', end='')
    while x % y and i < 1000: 
        x = x % y * 10
        i += 1
        print(x//y, end='')