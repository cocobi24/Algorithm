# https://www.acmicpc.net/problem/4378

from sys import stdin

keys = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\',
    'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'',
    'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'
        ]

while True :
    ip = stdin.readline().rstrip()
    if ip == '':
        break
    none = ['`', 'Q', 'A', 'Z', ' ']
    for s in ip :
        if s not in none :
            idx = keys.index(s)
            print(keys[idx-1], end='')
        else :
            print(s, end='')
    print()
