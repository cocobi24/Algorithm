# https://www.acmicpc.net/problem/11723

import sys
input = sys.stdin.readline
m = int(input())
s = set()

for _ in range(m) :
    cmd = input().rstrip().split()
    if len(cmd) == 1 :
        if cmd[0] == 'all' :
            s = set(i for i in range(1,21))
        elif cmd[0] == 'empty' :
            s = set()
    else :
        x = int(cmd[1])
        if cmd[0] == 'add' :
            s.add(x)
        elif cmd[0] == 'remove' :
            s.discard(x)
        elif cmd[0] == 'check' :
            if x in s:
                print(1)
            else :
                print(0)
        elif cmd[0] == 'toggle' :
            if x in s :
                s.remove(x)
            else :
                s.add(x)
