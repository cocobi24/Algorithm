# https://www.acmicpc.net/problem/5525

n = int(input())
m = int(input())
s = input()
cursor, cnt, answer = 0, 0, 0
target = 'IOI'

while cursor < (m - 1):
    if s[cursor:cursor + 3] == target:
        cnt += 1
        cursor += 2
        if cnt == n:
            answer += 1
            cnt -= 1
    else:
        cursor += 1
        cnt = 0

print(answer, end='')