# https://www.acmicpc.net/problem/2605

n = int(input())
student = list(map(int, input().split()))
line = [1]

for i in range(1, n) :
    temp_line = []
    for _ in range(student[i]) :
        temp = line.pop()
        temp_line.append(temp)
    temp_line.reverse()
    line.append(i + 1)
    line.extend(temp_line)
print(*line)