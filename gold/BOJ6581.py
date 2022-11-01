# https://www.acmicpc.net/problem/6581

import sys
input = sys.stdin
answers = []
temp = ""

for str in input :
    temp += str

for word in temp.split() :
    if word == '<br>' :
        answer = ' '.join(answers)
        answers = []
        print(answer)
    elif word == '<hr>':
        if len(answers) > 0:
            answer = ' '.join(answers)
            answers = []
            print(answer)
        print('-'*80)
    else:
        answers.append(word)
        answer = ' '.join(answers)
        if len(answer) > 80:
            answers.pop()
            answer = ' '.join(answers)
            print(answer)
            answers = []
            answers.append(word)

print(' '.join(answers))