# https://www.acmicpc.net/problem/33572

oneHole = ['A', 'a', 'b', 'D', 'd', 'e', 'g', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', '@']
def getHoleCount(s):
    if s in oneHole:
        return 1
    if s == 'B':
        return 2
    return 0

S = list(input().rstrip().replace(' ', ''))
cnt = 0
for s in S:
    cnt += getHoleCount(s)
print(cnt)