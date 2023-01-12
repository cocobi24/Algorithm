# https://www.acmicpc.net/problem/11816

n = input()
if n[0] == '0' and len(n) > 1:
    if n[1] == 'x' :
        print(int(n[2:], 16))
    else :
        print(int(n[1:], 8))
else :
    print(n)