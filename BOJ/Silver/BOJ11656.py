# https://www.acmicpc.net/problem/11656

answer = []
str = input()
l = len(str)

for i in range(l) :
    answer.append(str[i::])

answer = sorted(answer)
print(*answer, sep='\n', end='')