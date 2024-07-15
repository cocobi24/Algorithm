# https://www.acmicpc.net/problem/1449

n, l = map(int, input().split())
pipes = sorted(list(map(int, input().split())))
band = 0
answer = 0
for pipe in pipes :
    if pipe > band :
        band = pipe + (l-1)
        answer += 1

print(answer, end='')