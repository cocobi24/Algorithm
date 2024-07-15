# https://www.acmicpc.net/problem/11478

str = input()
l = len(str)
answer = {}

for i in range(l) :
    for j in range(l+1):
        answer[str[i:j]] = 1

answer = list(filter(None, answer))
print(len(answer), end='')