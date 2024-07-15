# https://www.acmicpc.net/problem/10709

import sys
input = sys.stdin.readline
h,w = map(int, input().split())
prediction = []
answer = []

for i in range(h) :
    row = list(input().rstrip())
    prediction.append([])
    for cell in row :
        prediction[i].append(cell)

for i in range(h) :
    answer.append([])
    cloud_flag = 0
    min = 0
    for cell in prediction[i] :
        if cell == 'c' :
            answer[i].append(0)
            cloud_flag = 1
            min = 0
        elif cloud_flag == 1 :
            min += 1
            answer[i].append(min)
        else :
            answer[i].append(-1)

for i in range(h) :
    for j in range(w) :
        print(answer[i][j], end=" ")
    print()