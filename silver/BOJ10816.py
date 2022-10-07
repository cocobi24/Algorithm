# https://www.acmicpc.net/problem/10816

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
answers = {i:0 for i in target}

for i in cards :
    if i in answers:
        answers[i] += 1
    else :
        continue

for i in target :
    if answers.get(i) is None :
        print(0, end=" ")
    else :
        print(answers.get(i), end=" ")