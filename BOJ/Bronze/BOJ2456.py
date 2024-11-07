# https://www.acmicpc.net/problem/2456

n = int(input())
vote = []
for i in range(1, 4):
    vote.append([0, 0, 0, 0, i])

for _ in range(n):
    a, b, c = map(int, input().split())
    vote[0][a-1] += 1
    vote[0][3] += a
    vote[1][b-1] += 1
    vote[1][3] += b
    vote[2][c-1] += 1
    vote[2][3] += c
    
vote.sort(key=lambda x: (-x[3], -x[2], -x[1]))
if vote[0][3] > vote[1][3] or (vote[0][2] != vote[1][2] and vote[0][1] != vote[1][1]):
    print(vote[0][4], vote[0][3])
else:
    print(0, vote[0][3])