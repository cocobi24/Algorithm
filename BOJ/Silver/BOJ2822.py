# https://www.acmicpc.net/problem/2822

scores = sorted([(int(input()), i+1) for i in range(8)], reverse=True)[:5]
total = 0
top = []
for i in range(5) :
    total += scores[i][0]
    top.append(scores[i][1])

print(total)
print(*sorted(top), end='')