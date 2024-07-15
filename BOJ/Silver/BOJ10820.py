# https://www.acmicpc.net/problem/10820

import sys
input = sys.stdin
temp = []

for str in input :
    s = list(str.rstrip('\n'))
    temp.append(s)

l = len(temp)

for i in range(l) :
    str = temp[i]
    answer = [0, 0, 0, 0]
    for s in str :
        check = ord(s)
        if check >= 97 and check <= 122:
            answer[0] += 1
        elif check >= 65 and check <= 90:
            answer[1] += 1
        elif check >= 48 and check <= 57 :
            answer[2] += 1
        elif check == 32 :
            answer[3] += 1
    print(*answer)