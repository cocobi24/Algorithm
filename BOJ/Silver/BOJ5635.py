# https://www.acmicpc.net/problem/5635

n = int(input())
answer = {}

for i in range(n) :
    str = input().split(' ')
    name = str[0]
    if len(str[1]) == 1 :
        str[1] = '0' + str[1]
    if len(str[2]) == 1 :
        str[2] = '0' + str[2]
    birth = ''.join(reversed(str[1:]))

    answer[name] = birth

answer = sorted(answer.items(), key= lambda x: (x[1], x[0]))
print(answer[-1][0])
print(answer[0][0], end='')