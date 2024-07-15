# https://www.acmicpc.net/problem/1110

n = int(input())
m = n
answer = 0
while True :
    answer += 1
    if n < 10 :
        n = '0' + str(n)
    nStr = list(map(int, str(n)))

    if sum(nStr) < 10 :
        n = int(str(nStr[1]) + str(sum(nStr)))
    else :
        n = int(str(nStr[1]) + str(sum(nStr))[1])

    if m == n :
        break

print(answer)