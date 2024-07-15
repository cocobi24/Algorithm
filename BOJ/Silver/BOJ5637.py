# https://www.acmicpc.net/problem/5637

import re
import sys
input = sys.stdin
temp = []
maxlen = 0
answer = ''
for str in input :
    str = re.sub('[=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', str.rstrip()).split()
    for i in range(len(str)) :
        temp.append(str[i])
temp.pop()

for s in temp :
    if len(s) > maxlen :
        maxlen = len(s)
        answer = s

print(answer.lower(), end='')