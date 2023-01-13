# https://www.acmicpc.net/problem/11726

n = int(input())
tile = [0] * 1001
tile[1] = 1
tile[2] = 2

for i in range(3, n+1) :
    tile[i] = tile[i-1] + tile[i-2]

answer = tile[n] % 10007
print(answer)