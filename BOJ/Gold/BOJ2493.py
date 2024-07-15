# https://www.acmicpc.net/problem/2493

n = int(input())
tower = list(map(int, input().split()))
answer = [0] * n
stack = []
for i in range(n):
    while stack:
        if tower[i] > tower[stack[-1][0]]:
            stack.pop()
        else:
            answer[i] = stack[-1][0] + 1
            break
    stack.append((i, tower[i]))
print(*answer)