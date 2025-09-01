# https://www.acmicpc.net/problem/3448

import sys
input = sys.stdin.readline

def get_integer_num(n):
    if n.is_integer():
        return int(n)
    return n

n = int(input())
for _ in range(n):
    s = ''
    try:
        while True:
            line = input().rstrip()
            if line == '':
                break
            s += line
    except EOFError:
        pass
    cnt = s.count('#')
    if cnt == 0:
        print("Efficiency ratio is 100%.")
    else:
        ans = 100 - cnt / len(s) * 100
        if ans.is_integer():
            print(f"Efficiency ratio is {get_integer_num(ans)}%.")
        else:
            print(f"Efficiency ratio is {get_integer_num(round(ans, 1))}%.")