# https://www.acmicpc.net/problem/2839

weight = int(input())
answer = 0
while weight >= 0 :
    if weight % 5 == 0 :
        answer += (weight // 5)
        print(answer)
        break
    weight -= 3
    answer += 1
else :
    print(-1)