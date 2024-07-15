# https://www.acmicpc.net/problem/20114

import sys
input = sys.stdin.readline
n, h, w = list(map(int, input().split()))
notes = [input().rstrip() for _ in range(h)]
answers = []
answer = ''
for i in range(h) :
    note = notes[i]
    l = len(notes[i])
    answers.append([])

    for j in range(w,l+w,w) :
        idx = j - w
        temp = set(note[idx:j])

        if len(temp) > 1 and '?' in temp :
            temp.remove('?')

        answers[i].append(temp.pop())

for i in range(n) :
    temp = set()
    for j in range(h) :
        temp.add(answers[j][i])

    if len(temp) > 1 and '?' in temp:
        temp.remove('?')
    answer += temp.pop()

print(answer, end='')