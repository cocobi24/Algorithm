# https://www.acmicpc.net/problem/26265

import sys
input = sys.stdin.readline
n = int(input())
answer = {}
for _ in range(n) :
    mentor, mentee = input().rstrip().split()
    if mentor not in answer :
        answer[mentor] = []
    answer[mentor].append(mentee)

mentor_list = sorted(answer)
for mentor in mentor_list :
    mentee_list = sorted(answer[mentor], reverse=True)
    for mentee in mentee_list :
        print(mentor, mentee)