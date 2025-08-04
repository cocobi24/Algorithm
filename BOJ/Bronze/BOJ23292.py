# https://www.acmicpc.net/problem/23292

import sys
input = sys.stdin.readline

birth = list(map(int, list(input().rstrip())))
n = int(input())

def getBioScore (date):
    yyyy = (birth[0] - date[0]) ** 2 + (birth[1] - date[1]) ** 2 + (birth[2] - date[2]) ** 2 + (
                birth[3] - date[3]) ** 2
    mmdd = ((birth[4] - date[4]) ** 2 + (birth[5] - date[5]) ** 2) * (
                (birth[6] - date[6]) ** 2 + (birth[7] - date[7]) ** 2)
    return yyyy * mmdd

score_set = {}
for _ in range(n):
    coDate = input().rstrip()
    date = list(map(int, list(coDate)))
    bioScore = getBioScore(date)

    if bioScore in score_set:
        score_set[bioScore].append(int(coDate))
    else:
        score_set[bioScore] = [int(coDate)]

maxScore = max(score_set.keys())
ans = sorted(score_set[maxScore])[0]
print(ans)