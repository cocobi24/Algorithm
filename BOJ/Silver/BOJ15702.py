# https://www.acmicpc.net/problem/15702

n,m = map(int, input().split())
scores = list(map(int, input().split()))
rank = {}
for i in range(m) :
    case = list(input().split())
    nums = int(case[0])
    score = case[1:]
    sum = 0

    for j in range(n) :
        if score[j] == 'O' :
            sum += scores[j]
    rank[nums] = sum

rank = sorted(rank.items(), key = lambda x: (-x[1], x[0]))
print(rank[0][0], rank[0][1])
print(rank)