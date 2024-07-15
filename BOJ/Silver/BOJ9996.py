# https://www.acmicpc.net/problem/9996

t=int(input())
patterns = input().rstrip()
pattern = patterns.split('*')
front = list(pattern[0])
rear = list(pattern[1])

for i in range(t):
    target=list(input())
    flag = 0

    if len(front)<=len(target):
        if front == target[:len(front)]:
            flag += 1
        target=target[len(front):]

    if len(rear) <= len(target):
        if rear == target[-len(rear):]:
            flag += 1

    if flag == 2:
        print('DA')
    else:
        print('NE')