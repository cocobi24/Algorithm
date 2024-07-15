# https://www.acmicpc.net/problem/10162

time = int(input())
timer = [300, 60, 10]
answer = {300: 0, 60: 0, 10: 0}

if time % 10 != 0:
    print(-1)
else :
    for i in timer :
        answer[i] = time // i
        time = time % i

    for i in answer :
        print(answer[i], end=" ")