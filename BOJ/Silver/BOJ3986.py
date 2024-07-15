# https://www.acmicpc.net/problem/3986

n = int(input())
answer = 0

for _ in range(n) :
    word = list(input())
    stack = [word[0]]

    for i in range(1, len(word)) :
        if stack != [] :
            prev = stack.pop()
        else :
            stack.append(word[i])
            continue

        if word[i] == prev :
            continue

        stack.append(prev)
        stack.append(word[i])

    if len(stack) == 0 :
        answer += 1

print(answer)