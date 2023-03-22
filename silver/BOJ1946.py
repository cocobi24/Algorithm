# https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    applicant = sorted([list(map(int, input().split())) for _ in range(n)])
    temp = applicant[0][1]
    count = 1

    for i in range(1, len(applicant)):
        if applicant[i][1] < temp:
            temp = applicant[i][1]
            count += 1

    print(count)