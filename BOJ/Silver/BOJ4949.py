# https://www.acmicpc.net/problem/4949

import sys
import re
from collections import deque
input = sys.stdin.readline

while True :
    queue = deque()
    s = input().rstrip()
    str = re.sub('[0-9a-zA-Zㄱ-힗- ]', '', s)

    if s[0] == '.' :
        break

    str = str.replace('.', '')
    str_list = list(str)
    l = len(str_list)

    for s in str_list :
        prev = ''
        if len(queue) > 0 :
            prev = queue.pop()
            queue.append(prev)

        if s == '(' or s == '[':
            queue.append(s)

        if (prev == '(' and s == ')') or (prev == '[' and s == ']'):
            queue.pop()
        elif (prev == '(' and s == ']') or (prev == '[' and s == ')'):
            break
        elif prev == '' and (s == ']' or s == ')'):
            queue.append(s)
            break

    if len(queue) == 0 :
        print("yes")
    else :
        print("no")