# https://www.acmicpc.net/problem/1057

n, jimin, hansu = map(int, input().split())
answer = 0
while jimin != hansu:
    jimin -= jimin // 2
    hansu -= hansu // 2
    answer += 1
print(answer)